import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "W": 3,  # Wild symbol count
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "W": 10,  # Wild symbol value
}

def check_winnings(columns, lines, bet, values):
    """
    This function checks the winnings for a given spin of the slot machine game.
    It takes in the columns, number of lines, bet amount, and symbol values as inputs.
    It returns the total winnings and the list of winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        is_wild = symbol == "W"
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != "W" and (symbol != symbol_to_check or is_wild):
                break
        else:
            if is_wild:
                symbol = columns[1][line]  # Use the next symbol instead of wild symbol
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    This function generates a random spin of the slot machine game.
    It takes in the number of rows, number of columns, and symbol counts as inputs.
    It returns a list of columns, where each column is a list of symbols.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    """
    This function prints the current spin of the slot machine game.
    It takes in the columns as input and prints them in a grid format.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    """
    This function prompts the user to enter a deposit amount and returns the amount as an integer.
    It checks that the amount is greater than 0 and that it is a valid number.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount  # Return the amount and exit the function
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")


def get_number_of_lines():
    """
    This function prompts the user to enter the number of lines to bet on and returns the number as an integer.
    It checks that the number is between 1 and the maximum number of lines.
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines  # Return the valid number of lines and exit the function
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")


def get_bet():
    """
    This function prompts the user to enter a bet amount and returns the amount as an integer.
    It checks that the amount is between the minimum and maximum bet amounts.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")


def spin(balance):
    """
    This function simulates a spin of the slot machine game.
    It prompts the user to enter the number of lines to bet on and the bet amount.
    It then generates a random spin and checks the winnings.
    It returns the net winnings (winnings - total bet).
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def play_bonus_round():
    """
    This function is not implemented.
    It can be used to add bonus round gameplay and features.
    """
    print("Welcome to the bonus round!")
    # ...
    # Add your bonus round gameplay and features


def main():
    """
    This function runs the game loop for the slot machine game.
    It prompts the user to deposit money and then spins the slot machine game.
    It also triggers the bonus round if the user's balance reaches a certain threshold.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer.lower() == "q":
            break
        balance += spin(balance)

        # Trigger the bonus round with a certain condition
        if balance >= 1000:
            answer = input("Do you want to play the bonus round? (y/n)")
            if answer.lower() == "y":
                play_bonus_round()

    print(f"You left with ${balance}")