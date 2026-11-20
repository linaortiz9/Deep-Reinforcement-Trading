def make_key(namespace: str, raw_key: str) -> str:
    return f'{namespace.strip()}:{raw_key.strip()}'
