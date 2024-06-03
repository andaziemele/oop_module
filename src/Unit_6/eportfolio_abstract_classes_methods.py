#
# implementation of abstract classes and methods
#

from abc import ABC, abstractmethod


class MainAccount(ABC):
    """Abstract base class for bank accounts."""

    def __init__(self, sort_code: str, account_number: str, balance=0):
        self.sort_code = sort_code
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        """Abstract method to deposit money"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method to withdraw money"""
        pass

    @abstractmethod
    def check_balance(self):
        """Abstract method to check account balance"""
        pass


class SavingsAccount(MainAccount):
    """Savings account subclass."""
    def deposit(self, amount):
        """Adds money to the account balance."""
        self.balance += amount
        print(
            f"£{amount} added to the account with sort code: {self.sort_code} and account number: {self.account_number}")

    def withdraw(self, amount):
        """Withdraws money to the account balance."""
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"£{amount} withdrawn from the account with sort code: {self.sort_code} and account number: {self.account_number}")
        else:
            print(
                f"Insufficient funds in the account with sort code: {self.sort_code} and account number: {self.account_number}")

    def check_balance(self):
        """Checks the current account balance."""
        print(
            f"Current balance in the account with sort code: {self.sort_code} and account number: {self.account_number}: £{self.balance}")


# Example usage
if __name__ == '__main__':
    savings_account = SavingsAccount("22-33-44", "123456789", 1000)

    savings_account.deposit(500)  # Added £500 into the account 123456789 with sort code 22-33-44
    savings_account.check_balance()  # Balance in the account 123456789 with sort code 22-33-44: £1500
    savings_account.withdraw(2000)  # Insufficient funds in the account 123456789 with sort code 22-33-44
    savings_account.withdraw(1000)  # Withdrew £1000 from the account 123456789 with sort code 22-33-44
    savings_account.check_balance()  # Balance in the account 123456789 with sort code 22-33-44: £500
