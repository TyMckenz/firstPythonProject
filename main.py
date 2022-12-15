MAX_LINES = 3
MAX_BET = 30
MIN_BET = 1


def deposit():
    while True:
        amount = input("How much would you like to put in? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more then 0")
        else:
            print("Please enter a number")
    return amount


def number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on ? (1, 2, 3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the designated number of lines")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        amount = input("What would yo like to bet for each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter valid bet")
    return amount


def main():
    balance = deposit()
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient funds. Current balance: ${balance}")
        else:
            break

    print(f"You are putting ${bet} on {lines} lines. Total: ${total_bet}")


main()
