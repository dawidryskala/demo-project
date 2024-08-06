# import os
# import sys
# from datetime import datetime
# from pathlib import Path
# from typing import Any, Dict

import pandas as pd


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a = 10
b = 5
print(add(a, b))
print(subtract(a, b))

dummy_data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value1",
    "key5": "value1",
    "key6": "value1",
    "key7": "value1",
    "key8": "value1",
}

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 89, 54],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)

df.head(2)
df.head(4)
