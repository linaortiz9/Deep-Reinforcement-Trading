class CacheStats:
    def __init__(self):
        self.hits = 0
        self.misses = 0

    @property
    def hit_ratio(self) -> float:
        total = self.hits + self.misses
        return round(self.hits / total, 4) if total else 0.0
