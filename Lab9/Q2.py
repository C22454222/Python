class Person(object):
   def __init__(self, fname, sname, address):
       self.f_name = fname
       self.s_name = sname
       self.address = address


   def change_address(self, new_address):
       self.address = new_address

   def __str__(self):
       return self.f_name + " "+ self.s_name + " lives at " + self.address
   
# (a)
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.sum1 = 0  # Initialize sum1 in __init__
        self.sum2 = 0  # Initialize sum2 in __init__

    def area(self):
        self.sum1 = self.length * self.width
        return self.sum1
    
    def perimeter(self):
        self.sum2 = 2 * (self.length + self.width)
        return self.sum2
    
    def __str__(self):
        return str(self.sum1) + " is the area of this rectangle and " + str(self.sum2) + " is the perimeter"

# (b)
class BankAccount:
    def __init__(self, iban, accNo, initial_funds=0):
        self.iban = iban
        self.account_number = accNo
        self.initial_funds = initial_funds
        self.transactions = []
    
    def withdraw(self, amount):
        if amount > self.initial_funds or amount < 0:
            print("Amount greater than funds available or the amount given is invalid")
            return self.initial_funds
        
        self.initial_funds -= amount
        self.transactions.append(("Withdraw", amount))
    
        if len(self.transactions) > 5:
            del self.transactions[0]
        return self.initial_funds
    
    def deposit(self, amount):
        if amount < 0:
            print("Invalid deposit amount")
            return self.initial_funds
        
        self.initial_funds += amount
        self.transactions.append(("Deposit", amount))
        if len(self.transactions) > 5:
            del self.transactions[0]

        return self.initial_funds

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


    





# main
"""
p1 = Person("John", "Smith", "1 Pinebrook street")
print(p1.f_name)
print(p1.s_name)
print(p1.address)

p1.change_address("5 Cottage Avenue")
print(p1)

# Create an instance of the Rectangle class
r1 = Rectangle(20, 10)

# Call the area and perimeter methods
r1.area()
r1.perimeter()

# Print the object by explicitly calling the __str__ method
print(r1.__str__())
"""