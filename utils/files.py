import json
import os.path
from pathlib import Path


def get_file_abs_path(*path) -> str:
    """Get absolute file path to file"""
    return os.path.join((Path(__file__).parents[1]), *path)

def load_from_json(*path) -> dict:
    """Load from json to dict"""
    with open(get_file_abs_path(*path), encoding='utf-8') as f:
        return json.load(f)
