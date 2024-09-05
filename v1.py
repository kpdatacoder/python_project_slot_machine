import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {"A": 5, "B": 4, "C": 3, "D": 2}
symbol_values = {"A": 10, "B": 5, "C": 2, "D": 1}

def check_winnings(columns, lines, bet, values):
    winnings, winning_lines = 0, []
    for line in range(lines):
        if all(column[line] == columns[0][line] for column in columns):
            winnings += values[columns[0][line]] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    return [[random.choice(all_symbols) for _ in range(rows)] for _ in range(cols)]

def print_slot_machine(columns):
    for row in range(ROWS):
        print(" | ".join(column[row] for column in columns))

def deposit():
    while (amount := input("What would you like to deposit? $")).isdigit():
        if (amount := int(amount)) > 0:
            return amount
        print("Amount must be greater than zero.")
    print("Please enter a valid number.")

def get_number_of_lines():
    while (lines := input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")).isdigit():
        if 1 <= (lines := int(lines)) <= MAX_LINES:
            return lines
        print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
    print("Please enter a valid number.")

def get_bet():
    while (amount := input("What would you like to bet on each line? $")).isdigit():
        if MIN_BET <= (amount := int(amount)) <= MAX_BET:
            return amount
        print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
    print("Please enter a valid number.")

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        if input("Press Enter to play (q to quit): ") == "q":
            break
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
            continue
        balance -= total_bet
        print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
        print(f"You won ${winnings} on lines: {', '.join(map(str, winning_lines))}" if winning_lines else "You didn't win on any lines.")
        balance += winnings
        print(f"Your remaining balance is ${balance}.")
    print(f"You left with ${balance}.")

main()
