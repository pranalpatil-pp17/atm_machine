# ATM Machine

This is a simple ATM Machine simulation program implemented in Python. The program allows a user to generate a PIN, deposit money, withdraw money, and check the balance. 

## Features

- **Generate PIN**: Set a 4-digit PIN for the account.
- **Deposit Money**: Deposit a specified amount into the account.
- **Withdraw Money**: Withdraw a specified amount from the account, if sufficient balance is available.
- **Check Balance**: Check the current balance of the account.

## Requirements

- Python 3.10.11

## How to Use

1. Clone the repository or download the `atm_machine.py` file.
2. Ensure you have Python installed on your system.
3. Run the program using the command:
    ```bash
    python atm_machine.py
    ```
4. Follow the on-screen prompts to interact with the ATM machine.

## Code Overview

The `Atm` class provides the main functionality of the ATM machine. 

### Methods

- `__init__(self)`: Initializes the ATM machine and calls the `menu` method.
- `menu(self)`: Displays the main menu and calls the appropriate method based on user input.
- `create_pin(self)`: Allows the user to set a 4-digit PIN.
- `deposit(self)`: Allows the user to deposit money into the account.
- `withdraw(self)`: Allows the user to withdraw money from the account.
- `check_balance(self)`: Allows the user to check the current balance of the account.

### Example Usage

Here's a quick example of how the program works:

```plaintext
Hi, How you want to proceed? Please select the action below!

    1. Generate pin
    2. Deposit money
    3. Withdraw money
    4. Check balance
    5. Exit
1
Please enter a four digit number to set a pin successfully: 1234
Pin created successfully!

Hi, How you want to proceed? Please select the action below!

    1. Generate pin
    2. Deposit money
    3. Withdraw money
    4. Check balance
    5. Exit
2
Please enter your pin: 1234
Enter the amount you want to deposit: 100
Deposit Successful!

Hi, How you want to proceed? Please select the action below!

    1. Generate pin
    2. Deposit money
    3. Withdraw money
    4. Check balance
    5. Exit
4
Please enter your pin: 1234
Your available balance is 100.0
