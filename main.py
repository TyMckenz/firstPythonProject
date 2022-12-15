import random

MAX_LINES = 3
MAX_BET = 30
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "*": 3,
    "#": 3,
    "&": 4,
    "@": 5
}

symbol_value = {
    "*": 5,
    "#": 4,
    "&": 3,
    "@": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


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


def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient funds. Current balance: ${balance}")
        else:
            break

    print(f"You are putting ${bet} on {lines} lines. Total: ${total_bet}")

    slots = spin_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Congratulations! You won ${winnings} on line: " *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if spin == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
