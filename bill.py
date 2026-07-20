from __future__ import annotations

import csv
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Dict, List

TAX_RATE = Decimal("0.12")


def calculate_bill(rows: List[Dict[str, str]]) -> Dict[str, Decimal]:
    subtotal = Decimal("0.00")
    for row in rows:
        quantity = Decimal(str(row.get("quantity", "0") or "0"))
        price = Decimal(str(row.get("price", "0") or "0"))
        subtotal += quantity * price

    subtotal = subtotal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    tax = (subtotal * TAX_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    total = (subtotal + tax).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {"subtotal": subtotal, "tax": tax, "total": total}


def read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def print_bill(rows: List[Dict[str, str]]) -> None:
    bill = calculate_bill(rows)
    print("=" * 28)
    print("BILL SOFTWARE")
    print("=" * 28)
    print(f"Subtotal: {bill['subtotal']:.2f}")
    print(f"Tax:      {bill['tax']:.2f}")
    print(f"Total:    {bill['total']:.2f}")


def main() -> None:
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "items.csv"
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    rows = read_csv(str(csv_file))
    print_bill(rows)


if __name__ == "__main__":
    main()
