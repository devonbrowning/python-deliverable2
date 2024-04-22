def fruit_market():
    print("Welcome to the GC Fruit Market!")
    user_name = input("What is your name?\n")
    print(f"Welcome {user_name}.")

    # Fruit inventory with prices
    fruit_prices = {
        1: ("Apple", 2),
        2: ("Grape", 1),
        3: ("Orange", 3)
    }

    fruit_inventory = {1: 0, 2: 0, 3: 0}

    buy_more = True
    while buy_more:
        print("Which Fruit would you like to buy?")
        for key, (fruit, price) in fruit_prices.items():
            print(f"{key}. {fruit} ${price}")

        choice = int(input("> "))
        if choice in fruit_prices:
            fruit, price = fruit_prices[choice]
            fruit_inventory[choice] += 1
            print(f"You bought 1 {fruit} at ${price}")

        response = input("Would you like to buy another piece of fruit? (y/n)\n")
        if response.lower() != 'y':
            buy_more = False

    # Print receipt
    print(f"\nOrder for {user_name}")
    subtotal = sum(fruit_inventory[key] * fruit_prices[key][1] for key in fruit_inventory)
    tax = subtotal * 0.05
    total = subtotal + tax

    for key, (fruit, price) in fruit_prices.items():
        print(f"{fruit_inventory[key]} {fruit}(s) at ${price} apiece")

    print(f"Sub Total: ${subtotal}")
    print(f"Tax (5%): ${tax}")
    print(f"Total: ${total}")

if __name__ == "__main__":
    fruit_market()