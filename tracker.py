import json
import argparse


try:
    with open("file.json", 'r') as f:
        expenses = json.load(f)
except FileNotFoundError as e:
    with open("file.json", 'w') as f:
        f.write("[]")


