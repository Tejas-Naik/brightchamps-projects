# Vending machine products and their prices (in cents)
products = {
    "Soda": 150,
    "Chips": 100,
    "Candy": 75,
    "Drink": 200
}

# Function to display available products
def display_products():
  print("\nAvailable Products:")
  for name, price in products.items():
    print(f"{name} - {price} cents")


# Function to calculate the total bill
def calculate_total(selected_products):
    total = 0
    for price in selected_products.values():
        total += price
    return total


# Function to simulate the vending machine
def vending_machine():
  print("🛒🛒🛒 Welcome to the Vending Machine! 🛒🛒🛒")
  display_products()

  selected_products = {}

  while True:
    choice = input("\nEnter the product name you want to purchase (or 'exit' to exit): ").capitalize()

    if choice == "Exit":
      break

    if choice in products:
      quantity = int(input(f"Enter the quantity of {choice} you want to purchase: "))
      selected_products[choice] = products[choice] * quantity
      print(f"You've selected {quantity} {choice}.")
    else:
      print("Invalid product name. Please enter a valid product.")

  # After the WHILE loop is ended,
  # Only if user selected atleast 1 product, we display the products list
  if len(selected_products) > 0:
    print(f"\nSelected products:")
    for name, total in selected_products.items():
      print(f"- {name}: {total} cents")

  # Activity - 3 (Optional)
  # Only if user selected atleast 1 product, we ask if user wants to get the bill
  if len(selected_products) > 0:
    bill_choice = input("\nDo you want to calculate the total bill? (yes/no): ")
    if bill_choice.lower() == "yes":
      total_amount = calculate_total(selected_products)
      print(f"\nTotal amount to pay: {total_amount} cents")
    else:
      print("\nThank you for your selections!")


# Run the vending machine simulation
vending_machine()
