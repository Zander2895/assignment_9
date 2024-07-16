orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Carol", "Cherry", 3)
]

# Function to print orders
def print_orders(orders):
    for order in orders:
        customer_name, product_name, quantity = order
        print(f"Customer: {customer_name}, Product: {product_name}, Quantity: {quantity}")

# Function to add a new order
def add_order():
    customer_name = input("Enter customer name: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    orders.append((customer_name, product_name, quantity))

# Print existing orders
print("Existing Orders:")
print_orders(orders)

# Ask user if they want to add more orders
while True:
    add_more = input("Do you want to add another order? (yes/no): ").lower()
    if add_more != 'yes':
        break
    add_order()

# Print updated orders
print("\nUpdated Orders:")
print_orders(orders)