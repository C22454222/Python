class WholeNumber:
    def __init__(self, value):
        if value < 0:
            print("Error: Cannot create a WholeNumber with a negative value.")
        else:
            self.value = value

    def __add__(self, other):
        result = self.value + other.value
        if result < 0:
            print("Error: Addition resulted in a negative value.")
        else:
            return WholeNumber(result)

    def __sub__(self, other):
        result = self.value - other.value
        if result < 0:
            print("Error: Subtraction resulted in a negative value.")
        else:
            return WholeNumber(result)

    def __mul__(self, other):
        result = self.value * other.value
        if result < 0:
            print("Error: Multiplication resulted in a negative value.")
        else:
            return WholeNumber(result)

    def __str__(self):
        return str(self.value)

# Sample code to demonstrate the WholeNumber class

# Creating instances of WholeNumber
x = WholeNumber(5)
y = WholeNumber(3)

# Performing operations
z_add = x + y  # Addition
z_sub = x - y  # Subtraction
z_mul = x * y  # Multiplication

# Printing results
print("x:", x)
print("y:", y)
print("x + y:", z_add)
print("x - y:", z_sub)
print("x * y:", z_mul)

# Creating WholeNumber with a negative value (should print an error message)
invalid_number = WholeNumber(-2)

# Performing subtraction resulting in a negative value (should print an error message)
invalid_result = x - WholeNumber(10)
