import json
import argparse

def read_file():
    try:
        with open("file.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        with open("file.json", 'w') as f:
            f.write("[]")
            return []

def add():
    


