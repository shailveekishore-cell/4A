# Class: CSE 1321L
# Section:BW3
# Term:Fall Semester 2026
# Instructor:Akash Keshav Bharati
# Name:Shailvee Kishore
# Assigment 4
def input_choice(low, high):
    choice = int(input("> "))
    while choice < low or choice > high:
        print(f"Please, enter an option between {low} and {high}")
        choice = int(input("> "))
    return choice


def input_money():
    amount = float(input("> "))
    while amount < 0:
        print("Please, enter a non-negative amount")
        amount = float(input("> "))
    return amount


def burgers():
    amount = 0.0
    while True:
        print()
        print("1. Big Owl Burger - Single ($5.99)")
        print("2. Big Owl Burger - Double ($7.99)")
        print("3. Return")
        choice = input_choice(1, 3)
        if choice == 1:
            print("1 Big Owl Burger - Single added")
            amount += 5.99
        elif choice == 2:
            print("1 Big Owl Burger - Double added")
            amount += 7.99
        else:
            return amount


def sides():
    amount = 0.0
    while True:
        print()
        print("1. Fries ($3.49)")
        print("2. Onion Rings ($2.99)")
        print("3. Get Back")
        choice = input_choice(1, 3)
        if choice == 1:
            print("1 Fries added")
            amount += 3.49
        elif choice == 2:
            print("1 Onion Rings added")
            amount += 2.99
        else:
            return amount


def drinks():
    amount = 0.0
    while True:
        print()
        print("1. Scrappy-Cola - Small ($2.49)")
        print("2. Scrappy-Cola - Medium ($2.79)")
        print("3. Scrappy-Cola - Large ($2.99)")
        print("4. Dr Owl - Small ($2.49)")
        print("5. Dr Owl - Medium ($2.79)")
        print("6. Dr Owl - Large ($2.99)")
        print("7. Return")
        choice = input_choice(1, 7)
        if choice == 1:
            print("1 Scrappy-Cola - Small added")
            amount += 2.49
        elif choice == 2:
            print("1 Scrappy-Cola - Medium added")
            amount += 2.79
        elif choice == 3:
            print("1 Scrappy-Cola - Large added")
            amount += 2.99
        elif choice == 4:
            print("1 Dr Owl - Small added")
            amount += 2.49
        elif choice == 5:
            print("1 Dr Owl - Medium added")
            amount += 2.79
        elif choice == 6:
            print("1 Dr Owl - Large added")
            amount += 2.99
        else:
            return amount


def order():
    subtotal = 0.0
    while True:
        print("Choose an option:")
        print("1. Burgers")
        print("2. Sides")
        print("3. Drinks")
        print("4. Check out")
        choice = input_choice(1, 4)
        if choice == 1:
            subtotal += burgers()
            print()
        elif choice == 2:
            subtotal += sides()
            print()
        elif choice == 3:
            subtotal += drinks()
            print()
        else:
            return subtotal


def calculate_tip(subtotal):
    print("Choose a tip option:")
    print("1. 18%")
    print("2. 20%")
    print("3. 25%")
    print("4. Custom")
    print("5. No Tip")
    choice = input_choice(1, 5)
    if choice == 1:
        return subtotal * 0.18
    elif choice == 2:
        return subtotal * 0.20
    elif choice == 3:
        return subtotal * 0.25
    elif choice == 4:
        print("Enter a custom tip amount:")
        return input_money()
    else:
        return 0.0


def calculate_tax(subtotal):
    return subtotal * 0.06


def print_total(subtotal, tip, tax):
    total = subtotal + tip + tax
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tip: ${tip:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


def main():
    subtotal = order()
    tip = calculate_tip(subtotal)
    tax = calculate_tax(subtotal)
    print_total(subtotal, tip, tax)


main()