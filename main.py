import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

symbol_values = {
    "A": 10,
    "B": 5,
    "C": 2,
    "D": 1
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    
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
        print(" | ".join(column[row] for column in columns))

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

def games(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
        else:
            balance -= total_bet
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("You didn't win on any lines.")
    balance += winnings
    print(f"Your remaining balance is: ${balance}")
    return balance

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press Enter to play (q to quit): ")
        if spin == "q":
            break
        balance = games(balance)
        
    print(f"You left with ${balance}")

main()
