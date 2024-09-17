import re

def get_last_segment(path):
    # Regex to match the last segment after the last forward slash
    match = re.search(r'[^/]+(?=/*$)', path)
    if match:
        return match.group(0)
    return None