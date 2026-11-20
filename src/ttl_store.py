import time

class TTLStore:
    def __init__(self, max_items: int = 256):
        self.max_items = max_items
        self._data = {}

    def purge_expired(self):
        now = time.monotonic()
        stale = [k for k, (_, exp) in self._data.items() if exp <= now]
        for k in stale:
            del self._data[k]
