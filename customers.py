# Reflection 1: I use .get() when a key may be absent, such as an optional field in imported customer data, because it lets me choose a useful fallback. I use bracket notation when a key is required and its absence should be treated as an error. My rule of thumb is to use .get() for optional data and brackets for required data.
# Reflection 2: Building a sales summary by region reminds me of an Excel PivotTable or SUMIF summary. Python can repeat the same calculation automatically across many files or records, which is useful when a dataset is too large or changes too often to summarize by hand.

# Exercise 1: One customer
customer = {
    "name": "Alice Morgan",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 2400.00,
}

print("EXERCISE 1: ONE CUSTOMER")
print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("Year-to-date spend:", customer["ytd_spend"])
print("Full customer record:", customer)

# Exercise 2: Add, update, and delete fields
print("\nEXERCISE 2: UPDATE AND ADD")
customer["phone"] = "555-0102"
print("After adding phone:", customer)
customer["tier"] = "platinum"
print("After updating tier:", customer)
del customer["email"]
print("After deleting email:", customer)

# Exercise 3: Safe lookup for a missing field
print("\nEXERCISE 3: SAFE LOOKUP")
email = customer.get("email", "no email on file")
print("Email from .get():", email)
try:
    print(customer["email"])
except KeyError as error:
    print("Bracket lookup raised KeyError:", error)

# Exercise 4: Iterate over key/value pairs
print("\nEXERCISE 4: ITERATE")
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), iterating over a dictionary gives only its keys, not key/value pairs.
for key in customer:
    print("Key only:", key)

# Exercise 5: Use the customer's tier to price a purchase
print("\nEXERCISE 5: LOOKUP TABLE")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
purchase_price = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase_price * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price on ${purchase_price:.2f}: ${final_price:.2f}")

# Exercise 6: Apply tier discounts to several customers
print("\nEXERCISE 6: LIST OF CUSTOMERS")
customers = [
    {"name": "Jordan Lee", "tier": "bronze"},
    {"name": "Morgan Chen", "tier": "silver"},
    {"name": "Taylor Rivera", "tier": "gold"},
]
purchase_price = 300
for customer_record in customers:
    rate = tier_discounts.get(customer_record["tier"], 0)
    discount_amount = purchase_price * rate
    final_price = purchase_price - discount_amount
    print(
        f"{customer_record['name']} ({customer_record['tier']}): "
        f"discount ${discount_amount:.2f}; final price ${final_price:.2f}"
    )

# Exercise 7: Find products with low stock
print("\nEXERCISE 7: NESTED CATALOG")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} — {details['stock']} remaining")

# Exercise 8: Summarize sales by region
print("\nEXERCISE 8: SALES BY REGION")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + transaction["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
