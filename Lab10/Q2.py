class BankAccount:
    def __init__(self, iban, accNo, initial_funds=0):
        # Constructor for the BankAccount class
        self.iban = iban  # Assigning IBAN (International Bank Account Number)
        self.account_number = accNo  # Assigning Account Number
        self.initial_funds = initial_funds  # Assigning initial funds to the account
        self.transactions = []  # Initializing an empty list to store transactions
    
    def withdraw(self, amount):
        # Method to withdraw funds from the account
        if amount > self.initial_funds or amount < 0:
            # Checking if the withdrawal amount is greater than available funds or negative
            print("Amount greater than funds available or the amount given is invalid")
            return self.initial_funds  # Return the current funds if withdrawal is not possible
        
        self.initial_funds -= amount  # Subtracting the withdrawal amount from initial funds
        self.transactions.append(("Withdraw", amount))  # Adding the withdrawal transaction to the list
        
        if len(self.transactions) > 5:
            del self.transactions[0]  # Deleting the oldest transaction if there are more than 5
        return self.initial_funds  # Return the updated funds after withdrawal
    
    def deposit(self, amount):
        # Method to deposit funds into the account
        if amount < 0:
            # Checking if the deposit amount is negative
            print("Invalid deposit amount")
            return self.initial_funds  # Return the current funds if deposit is not possible
        
        self.initial_funds += amount  # Adding the deposit amount to initial funds
        self.transactions.append(("Deposit", amount))  # Adding the deposit transaction to the list
        
        if len(self.transactions) > 5:
            del self.transactions[0]  # Deleting the oldest transaction if there are more than 5
        
        return self.initial_funds  # Return the updated funds after deposit

class MinBalance(BankAccount):
    def __init__(self, iban, accNo, initial_funds=0, minBalance=0):
        # Constructor for the MinBalance class, which inherits from BankAccount
        super().__init__(iban, accNo, initial_funds)  # Calling the constructor of the parent class
        self.minBalance = minBalance  # Assigning minimum balance for the account

    def withdraw(self, amount):
        # Method to withdraw funds from the account with minimum balance constraint
        if amount < 0 or amount > self.initial_funds - self.minBalance:
            # Checking if the withdrawal amount is negative or exceeds available funds after maintaining minimum balance
            print("Amount greater than funds available or the amount given is invalid or amount leaves funds less than the minimum balance")
            return self.initial_funds  # Return the current funds if withdrawal is not possible

        self.initial_funds -= amount  # Subtracting the withdrawal amount from initial funds
        self.transactions.append(("Withdraw", amount))  # Adding the withdrawal transaction to the list
        
        if len(self.transactions) > 5:
            del self.transactions[0]  # Deleting the oldest transaction if there are more than 5
        
        return self.initial_funds  # Return the updated funds after withdrawal

        
# Test the BankAccount class
b1 = BankAccount("IE1234", "12345", 1000)

# Initial state
print("Initial funds:", b1.initial_funds)
print("Transactions:", b1.transactions)

# Test deposit
b1.deposit(500)
print("Funds after deposit:", b1.initial_funds)
print("Transactions after deposit:", b1.transactions)

# Test invalid deposit
b1.deposit(-200)
print("Funds after invalid deposit:", b1.initial_funds)
print("Transactions after invalid deposit:", b1.transactions)

# Test valid withdrawal
b1.withdraw(300)
print("Funds after valid withdrawal:", b1.initial_funds)
print("Transactions after valid withdrawal:", b1.transactions)

# Test MinBalance class
b2 = MinBalance("US5678", "67890", 2000, minBalance=1000)

# Test valid withdrawal with minimum balance constraint
b2.withdraw(1500)
print("Funds after valid MinBalance withdrawal:", b2.initial_funds)
print("Transactions after valid MinBalance withdrawal:", b2.transactions)