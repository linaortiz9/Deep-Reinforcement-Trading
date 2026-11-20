import json

def encode_payload(obj) -> str:
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)
