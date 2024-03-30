# Define a new class named NewClass, inheriting from the base class 'object'
class NewClass(object):

    # Constructor method (__init__) with a default parameter 'param_int' set to 1
    def __init__(self, param_int=1):

        # Initialize an instance variable 'the_int' with the value of 'param_int'
        self.the_int = param_int

        # Check if 'param_int' is even or odd and set the 'parity' instance variable accordingly
        if param_int % 2 == 0:
            self.parity = 'even'
        else:
            self.parity = 'odd'
    
    # Define a method named 'process' that takes another instance ('instance') of the class as a parameter
    def process(self, instance):

        # Calculate the sum of the 'the_int' attribute of the current instance and 'instance'
        sum_int = self.the_int + instance.the_int

        # Check if the sum is negative, even, or odd, and return the corresponding string
        if sum_int < 0:
            return 'negative'
        elif sum_int % 2 == 0:
            return 'even'
        else:
            return 'odd'
    
    # Define a special method (__str__) to provide a string representation of the object
    def __str__(self):

        # Return a formatted string containing the value of 'the_int' and its parity
        return 'Value {} is {}'.format(self.the_int, self.parity)

# Create instances of the NewClass with different parameters
inst1 = NewClass(4)
inst2 = NewClass(-5)
inst3 = NewClass()  # Uses the default value for 'param_int', which is 1

# Print the string representation of inst1 using the __str__ method
print(inst1)
# Print the 'parity' attribute of inst1
print(inst1.parity)
# Call the 'process' method on inst1 with inst2 as a parameter and print the result
print(inst1.process(inst2))
# Call the 'process' method on inst3 with inst1 as a parameter and print the result
print(inst3.process(inst1))
