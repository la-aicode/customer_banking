# Import the Account class from the Account.py file
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: The updated CD account balance after adding the interest earned,
               and the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd_account = Account(balance, 0)

    # Calculate interest earned (simple interest for the period)
    interest_earned = (balance * (interest_rate / 100) * (months / 12))

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set_balance method using the instance of the Account class.
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set_interest method using the instance of the Account class.
    cd_account.set_interest(interest_rate)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
