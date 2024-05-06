class Checkbook:
    """
    A simple class representing a checkbook to manage deposits, withdrawals, and balance.

    Attributes:
    - balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes the Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the checkbook.

        Parameters:
        - amount (float): The amount to deposit.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be positive.")
            else:
                self.balance += amount
                print("Deposited ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

    def withdraw(self, amount):
        """
        Withdraw funds from the checkbook, if sufficient funds are available.

        Parameters:
        - amount (float): The amount to withdraw.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be positive.")
            elif amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

    def get_balance(self):
        """
        Print the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    The main function to interact with the Checkbook class.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
