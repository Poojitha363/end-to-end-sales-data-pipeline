#!/usr/bin/env python3
"""Generate a synthetic sales dataset and save it as a CSV file."""

from __future__ import annotations

import csv
import random
import sys
from datetime import date
from pathlib import Path
from typing import Dict

try:
    from faker import Faker
except Exception:
    print("Faker library is required. Install it with: pip install Faker")
    sys.exit(1)

# -------------------- Configuration --------------------
# Number of records to generate.
NUM_RECORDS = 10_000

# Output path. The script creates the parent folder if it is missing.
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "raw"
OUTPUT_FILE = OUTPUT_DIR / "sales_data.csv"

# Date range for generated orders.
START_DATE = date(2024, 1, 1)
END_DATE = date(2025, 12, 31)

# Column names in the required order.
FIELDNAMES = [
    "order_id",
    "order_date",
    "customer_name",
    "city",
    "state",
    "product",
    "category",
    "quantity",
    "price",
    "discount",
    "total_amount",
    "payment_method",
    "sales_person",
]

# Product catalog organized by realistic categories.
PRODUCTS_BY_CATEGORY = {
    "Electronics": [
        "Smartphone",
        "Laptop",
        "Tablet",
        "Wireless Earbuds",
        "Smart TV",
        "Bluetooth Speaker",
        "Gaming Console",
        "Camera",
    ],
    "Furniture": [
        "Sofa",
        "Dining Table",
        "Office Chair",
        "Bed Frame",
        "Bookshelf",
        "Coffee Table",
    ],
    "Grocery": [
        "Organic Milk",
        "Cereal Box",
        "Olive Oil",
        "Coffee Beans",
        "Snack Pack",
        "Canned Beans",
    ],
    "Clothing": [
        "T-Shirt",
        "Jeans",
        "Jacket",
        "Sneakers",
        "Dress",
        "Sweater",
    ],
    "Sports": [
        "Yoga Mat",
        "Tennis Racket",
        "Football",
        "Fitness Tracker",
        "Basketball Shoes",
    ],
}

# Common payment methods.
PAYMENT_METHODS = ["Credit Card", "Debit Card", "Cash", "Mobile Pay", "Net Banking"]


# -------------------- Helper Functions --------------------

def ensure_output_dir(path: Path) -> None:
    """Create the output directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)


def generate_order_id(index: int) -> str:
    """Create a deterministic, zero-padded order ID."""
    return f"ORD-{index:07d}"


def generate_order_date(fake: Faker) -> str:
    """Generate a realistic order date between the allowed range."""
    return fake.date_between_dates(date_start=START_DATE, date_end=END_DATE).isoformat()


def choose_product_and_category() -> tuple[str, str]:
    """Pick a category and a matching product from the catalog."""
    category = random.choice(list(PRODUCTS_BY_CATEGORY.keys()))
    product = random.choice(PRODUCTS_BY_CATEGORY[category])
    return product, category


def generate_price() -> float:
    """Generate a unit price between 100 and 50,000."""
    return round(random.uniform(100.0, 50_000.0), 2)


def generate_quantity() -> int:
    """Generate a quantity between 1 and 10."""
    return random.randint(1, 10)


def generate_discount() -> float:
    """Generate a discount percentage between 0 and 30."""
    return round(random.uniform(0.0, 30.0), 2)


def calculate_total_amount(quantity: int, price: float, discount_pct: float) -> float:
    """Calculate the discounted total amount for one order line."""
    discounted_total = quantity * price * (1 - discount_pct / 100)
    return round(discounted_total, 2)


def build_record(index: int, fake: Faker, sales_people: list[str]) -> Dict[str, object]:
    """Create one sales record as a dictionary."""
    product, category = choose_product_and_category()
    quantity = generate_quantity()
    price = generate_price()
    discount = generate_discount()

    return {
        "order_id": generate_order_id(index),
        "order_date": generate_order_date(fake),
        "customer_name": fake.name(),
        "city": fake.city(),
        "state": fake.state(),
        "product": product,
        "category": category,
        "quantity": quantity,
        "price": price,
        "discount": discount,
        "total_amount": calculate_total_amount(quantity, price, discount),
        "payment_method": random.choice(PAYMENT_METHODS),
        "sales_person": random.choice(sales_people),
    }


def write_csv(file_path: Path, rows: list[Dict[str, object]]) -> None:
    """Write the generated records to a CSV file."""
    with file_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


# -------------------- Main Entry Point --------------------

def main() -> None:
    """Generate the sales dataset and save it to disk."""
    fake = Faker()
    sales_people = [fake.name() for _ in range(12)]

    ensure_output_dir(OUTPUT_DIR)

    rows: list[Dict[str, object]] = []
    for index in range(1, NUM_RECORDS + 1):
        rows.append(build_record(index, fake, sales_people))

    write_csv(OUTPUT_FILE, rows)

    print("Dataset generated successfully")
    print(f"Number of rows: {len(rows)}")
    print(f"File location: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
