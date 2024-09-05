# Slot Machine Game

This is a simple slot machine game written in Python. The player deposits money, places bets on multiple lines, and spins the slot machine. If matching symbols align on the selected lines, the player wins money based on the symbol values. The game continues until the player chooses to quit or runs out of money.

## How to Play

1. **Deposit Money**: Enter the amount you would like to deposit to start playing.
2. **Select Number of Lines**: Choose how many lines (1-3) you want to bet on.
3. **Place Bet**: Enter your bet amount for each line. The total bet is calculated based on the number of lines you bet on.
4. **Spin**: The slot machine will randomly generate symbols, and if matching symbols appear across the chosen lines, you win! Winnings are based on the symbol values.
5. **Repeat or Quit**: After each spin, you can choose to keep playing or quit the game.

## Game Rules

- **Rows**: 3 rows
- **Columns**: 3 columns
- **Symbols**:
  - `A`: 5 occurrences, value = 10
  - `B`: 4 occurrences, value = 5
  - `C`: 3 occurrences, value = 2
  - `D`: 2 occurrences, value = 1
- **Maximum Lines to Bet**: 3
- **Minimum Bet per Line**: $1
- **Maximum Bet per Line**: $100

## How to Run

1. Make sure you have Python installed on your system.
2. Download the script file `main.py`.
3. Run the script:
   ```bash
   python main.py
