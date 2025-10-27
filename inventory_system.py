import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(f"Invalid input types: item={item}, qty={qty}")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning(f"Attempted to remove non-existent item: {item}")

def get_qty(item):
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)

def save_data(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)

def print_data():
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

def check_low_items(threshold=5):
   
    return [item for item, qty in stock_data.items() if qty < threshold]

def main():
    logging.basicConfig(level=logging.INFO)

    add_item("apple", 10)
    add_item("banana", -2)
    add_item("ten", 123)  # valid input now

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    print("eval used")


main()