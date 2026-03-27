def add_products(inventory):
    name = input("Enter the name of the product: ")
    price = input("Enter the price: ")
    amount = input("Enter the amount: ")

    products = {
        "name": name,
        "price": price,
        "amount": amount
    }

    inventory.append(products)
    print(f"Product {name} added sucesfully")
    return products

def show_product(inventory):
    if not inventory:
        print("Product not found. Register it.")

    print("\n" + "-" * 50)
    print(f" {'name':<20} {'price':>20} {'amount':>20}")
    print("-" * 50)

    for product in inventory:
        print(f"{product['name']:<20} {product['price']:>20} {product['amount']:>20}")

    print("-" * 50)
    print(f"Total of products : {len(inventory)}\n")

subtotal = lambda product: product["price"] * product["amount"]

def calculate_stats(inventory):
    totals_price = sum(subtotal['price']for product in inventory)
    totals_amount = sum(product['amount']for product in inventory)

    expensive = max(inventory, key=lambda product: product['price'])
    less_expensive = min(inventory, key=lambda product: product['price'])

    return {
        "total_units":    totals_amount,
        "value_total":         totals_price,
        "most_expensive_product":   (expensive["name"],    expensive["price"]),
        "product_less_expensive": (less_expensive["name"], less_expensive["price"]),
    }

def show_stats(inventory):
    stats = calculate_stats(inventory)

    if stats is None:
        print("There is no data; the inventory is empty..")
        return

    name_expensive,   price_expensive   = stats["most_expensive_product"]
    name_minexpensive,   price_minexpensive   = stats["product_less_expensive"]

    print("\n")
    print("           INVENTORY STATISTICS")
    print("═" * 44)
    print(f"  Total units in stock: {stats['total_units']:>10}")
    print(f"  Total inventory value: ${stats['value_total']:>20,.2f}")
    print(f"  Most expensive product         : {name_expensive} (${price_expensive:,.0f})")
    print(f"  Less expensive product         : {name_minexpensive} (${price_minexpensive:,.0f})")

    
    print("\n   Subtotals by product ")
    for product in inventory:
        print(f"{product['name']:<22} ${subtotal(product):>10,.0f}")
    print("═" * 44 + "\n")