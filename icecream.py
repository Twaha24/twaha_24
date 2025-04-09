def calculate_ice_cream_price():
    """Calculates the total price of an ice cream order based on user input."""

    # Prices (you can adjust these)
    prices = {
        "cup": 1.50,
        "cone": 2.00,
        "scoop": 1.00,
        "flake": 0.50,
        "sprinkles": 0.25,
        "strawberry": 0.75,
    }

    # 1. Container Choice (with validation)
    while True:
        container = input("Would you like a cup or a cone? (cup/cone): ").lower()
        if container in ("cup", "cone"):
            break
        else:
            print("Invalid container choice. Please enter 'cup' or 'cone'.")

    # 2. Scoop Count (with validation)
    while True:
        try:
            scoops = int(input("How many scoops would you like (1-4)? "))
            if 1 <= scoops <= 4:
                break
            else:
                print("Invalid scoop count. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 3. Toppings (using boolean input)
    flake = input("Would you like a flake? (yes/no): ").lower() == "yes"
    sprinkles = input("Would you like chocolate sprinkles? (yes/no): ").lower() == "yes"
    strawberry = input("Would you like a strawberry? (yes/no): ").lower() == "yes"

    # Calculate Price
    total_price = prices[container] + (scoops * prices["scoop"])

    if flake:
        total_price += prices["flake"]
    if sprinkles:
        total_price += prices["sprinkles"]
    if strawberry:
        total_price += prices["strawberry"]

    # Output the Order and Total Price
    print("\nYour Ice Cream Order:")
    print(f"- Container: {container.capitalize()}")
    print(f"- Scoops: {scoops}")
    if flake:
        print("- Flake: Yes")
    if sprinkles:
        print("- Chocolate Sprinkles: Yes")
    if strawberry:
        print("- Strawberry: Yes")

    print(f"\nTotal Price: ${total_price:.2f}")


# Run the program
if __name__ == "__main__":
    calculate_ice_cream_price()