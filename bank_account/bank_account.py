class BankAccount:
    """Represents a bank account.

    Allows users to manage their bank account by making deposits, withdrawals, and checking the balance.
    """
    def __init__(self, owner_name: str, balance: float = 0):
        """Initializes a new bank account.

        Args:
            owner_name (str): The new owner's name.
            balance (float): The current balance in $, default is 0.
        """
        self.owner_name: str = owner_name
        self.balance: float = balance

    def deposit(self, amount: float) -> float:
        """Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit. Must be greater than 0.

        Returns:
            float: The updated account balance.

        Raises:
            TypeError: If the amount is not int or float type.
            ValueError: If the amount less or equal 0.
        """
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("\nThe amount must be a numeric value.")
            elif amount <= 0:
                raise ValueError("\nThe amount must be greater than 0.")
        except (TypeError, ValueError) as e:
            print(str(e))
            return self.balance

        self.balance += amount
        print(f"\nDeposited {amount:.2f}$. New balance: {self.balance:.2f}$.")
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraws the specified amount from the account balance.

        Args:
            amount (float): The amount to withdraw. Must be greater than 0 and not exceed the current balance.

        Returns:
            float: The updated account balance.

        Raises:
            TypeError: If the amount is not int or float type.
            ValueError: If the amount less or equal 0 or exceed the current balance.
        """
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("\nThe amount must be a numeric value.")
            elif amount <= 0:
                raise ValueError("\nThe amount can not be less than 0.")
            elif amount > self.balance:
                raise ValueError(f"\nInsufficient funds! Available balance: {self.balance:.2f}$.")
        except (TypeError, ValueError) as e:
            print(str(e))
            return self.balance

        self.balance -= amount
        print(f"\nWithdrawn {amount:.2f}$. New balance: {self.balance:.2f}$.")
        return self.balance

    def get_balance(self) -> None:
        """Prints the current balance."""
        print(f"\nCurrent balance: {self.balance:.2f}$.")


if __name__ == "__main__":
    bank_account = BankAccount("Kirill")
    bank_account.get_balance()
    bank_account.deposit(-100)
    bank_account.deposit(0)
    bank_account.deposit("adgfasdf")
    bank_account.deposit(10)
    bank_account.withdraw(9.5100000)
    bank_account.get_balance()
    bank_account.withdraw("sdgsdg")
    bank_account.withdraw(100)
    bank_account.withdraw(0.49)
    bank_account.get_balance()
