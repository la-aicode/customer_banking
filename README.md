# Account Management Program

This program provides a system for creating and managing various account types, including Savings and Certificate of Deposit (CD) accounts. It allows users to calculate interest based on input parameters, update account balances, and display results.

## Features
- **Account Class**: Basic class to create accounts, manage balances, and set interest rates.
- **Savings Account Functionality**: Calculates interest on a savings account for a specified period, updates the balance, and displays the results.
- **CD Account Functionality**: Calculates interest on a CD account over a specific term, updates the balance, and displays the interest earned.
- **User Interaction**: Allows users to input balances, interest rates, and account terms and view calculated interest and updated balances.

## Files and Structure

### `Account.py`
This module contains the `Account` class, which provides foundational methods for managing an account:
- **Methods**:
  - `__init__(balance, interest)`: Initializes the account with a specified balance and interest rate.
  - `set_balance(balance)`: Sets the account balance.
  - `get_balance()`: Returns the current balance.
  - `set_interest(interest)`: Sets the account’s interest rate.
  - `get_interest()`: Returns the current interest rate.
  - `deposit(amount)`: Adds a specified amount to the account balance.
  - `withdraw(amount)`: Deducts a specified amount if sufficient funds are available.
  - `apply_interest()`: Applies the interest rate to the account balance.

### `savings_account.py`
This module defines the `create_savings_account` function, which calculates the interest earned on a savings account:
- **Function**:
  - `create_savings_account(balance, interest_rate, months)`: 
    - **Arguments**: 
      - `balance` - initial savings account balance.
      - `interest_rate` - APR interest rate for the savings account.
      - `months` - duration in months to calculate interest for.
    - **Returns**: The updated balance after adding interest earned and the interest earned itself.

### `cd_account.py`
This module contains the `create_cd_account` function, which calculates interest on a Certificate of Deposit (CD) account:
- **Function**:
  - `create_cd_account(balance, interest_rate, months)`: 
    - **Arguments**:
      - `balance` - initial CD account balance.
      - `interest_rate` - APR interest rate for the CD account.
      - `months` - duration in months for calculating interest.
    - **Returns**: The updated CD account balance after interest and the interest earned.

### `customer_banking.py`
This script serves as the main entry point for the program, managing user interaction and invoking the `create_savings_account` and `create_cd_account` functions:
- **Prompts**:
  - For initial balance, interest rate, and months for both savings and CD accounts.
- **Displays**:
  - Interest earned and updated balances for both account types.

## Usage

1. **Clone the Repository**: Clone the repository containing the code files (`Account.py`, `savings_account.py`, `cd_account.py`, `customer_banking.py`).

2. **Run the Program**: Execute `customer_banking.py` to start the program.

    ```bash
    python customer_banking.py
    ```

3. **Input Required Information**: Follow the prompts to enter:
   - Initial balances for both the savings and CD accounts.
   - Annual interest rates for each account type.
   - Term (in months) for the savings and CD accounts.

4. **View Results**: The program will output the interest earned and the updated balance for both account types.

## Example Interaction
```
Enter the initial balance for the savings account: 1000
Enter the annual interest rate for the savings account (in %): 5
Enter the number of months for the savings account: 12
Interest earned on the savings account: $50.00
Updated savings account balance: $1050.00

Enter the initial balance for the CD account: 2000
Enter the annual interest rate for the CD account (in %): 3
Enter the number of months for the CD account: 12
Interest earned on the CD account: $60.00
Updated CD account balance: $2060.00
```

## Project Structure

```plaintext
.
├── Account.py              # Contains the Account class definition
├── cd_account.py           # Contains the function for creating and managing a CD account
├── savings_account.py      # Contains the function for creating and managing a savings account
├── customer_banking.py     # Main script to run the program and manage user interaction
└── README.md               # Project documentation
```

## Dependencies
- Python 3.x

## License
This project is licensed under the MIT License.

---

