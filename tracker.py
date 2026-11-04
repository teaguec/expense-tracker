import json
import argparse
import sys

def read_file():
    try:
        with open("file.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        with open("file.json", 'w') as f:
            f.write("[]")
            return []

def add():
    desc = sys.argv[2]
    amount = sys.argv[3]
    data = read_file()
    data.append({"description": desc, "amount": amount})
    with open ("file.json", 'w') as f:
        json.dump(data, f, indent=4)

    
if sys.argv[1] == "add":
    add()
