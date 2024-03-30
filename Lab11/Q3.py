"""
Q3. Write a class for linear equations. A generic linear equation is of the form y = mx + b where m and b are constants.
Include the following methods: 
(a) __init__, __str__. 
(b) value(x), which returns the value of the equation given x.
(c) compose(LinearEquation) that composes two linear equations. That is, if y = ax + b and z = cx + d, then y(z)= (a*c)x +(a*d + b) 
and will be called as y.compose(z). Note that the compose operation is not commutative. 
(d) add returns the sum of two linear equations. That is, if y = ax + b and z = cx + d, then y + z = (a + c)x + (b + d).
"""

class linear(object):
    def __init__(self, m, b): # (a)
        self.m = m
        self.b = b
    
    def __str__(self): # (a)
        return f"y = {self.m}x + {self.b}"
    
    def x(self,x): # (b)
        return self.m * x + self.b
    
    def compose(self, other):
        if not isinstance(other,linear):
            raise ValueError("There needs to be two equations to compose dummy")
        else:
            composedM = self.m * other.m
            composedB = self.m * other.b + self.b

            return linear(composedM,composedB)
    
    def add(self, other):
        if not isinstance(other,linear):
            raise ValueError("There needs to be two equations to add dummy")
        else:
            addedM = self.m + other.m
            addedB = self.b + other.b

            return linear(addedM, addedB)
    
    
# Sample code to demonstrate the LinearEquation class

# Creating instances of LinearEquation
equation1 = linear(2, 3)
equation2 = linear(-1, 5)

# Printing equations
print("Equation 1:", equation1)
print("Equation 2:", equation2)

# Calculating values
x_value = 4
value1 = equation1.x(x_value)
value2 = equation2.x(x_value)
print(f"Value of Equation 1 at x={x_value}: {value1}")
print(f"Value of Equation 2 at x={x_value}: {value2}")

# Composing equations
composed_equation = equation1.compose(equation2)
print("Composed Equation:", composed_equation)

# Adding equations
added_equation = equation1.add(equation2)
print("Added Equation:", added_equation)