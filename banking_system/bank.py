from banking_system import SavingsAccount, CheckingAccount

class Bank:
    """A class representing a bank with various account types."""

    def __init__(self):
        self.accounts = []

    # todo: Add the following method(s):
    #       create_account

    def create_account(self, account_type, account_number, account_holder_name, balance, **kwargs):
        """
        Creates a new account with given account type, account number, account holder name, balance, and interest rate 
        or overdraft limit depending upon the account type
        """
        if account_type == "SavingsAccount":
            interest_rate = kwargs["interest_rate"]
            account = SavingsAccount(account_number, account_holder_name, balance, interest_rate)
            self.accounts.append(account)
        
        elif account_type == "CheckingAccount":
            overdraft_limit = kwargs["overdraft_limit"]
            account = CheckingAccount(account_number, account_holder_name, balance, overdraft_limit)
            self.accounts.append(account)

    def delete_account(self, account_number):
        """Deletes an account with the given account number.

        Args:
            account_number (str): The account number of the account to delete.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return
        print("Account not found.")

    def find_account(self, account_number):
        """Finds an account with the given account number.

        Args:
            account_number (str): The account number to search for.

        Returns:
            Account or None: Returns the account if found, otherwise None.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None

    def list_accounts(self):
        """Displays the details of all accounts."""
        for account in self.accounts:
            account.display()
            print()
