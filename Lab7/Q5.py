"""
5. Fractions: You can express a fraction as a tuple: (numerator, denominator). 
(a) Write a function that adds two fractions that are passed as tuples. 
(b) Write a function that multiplies two fractions that are passed as tuples

"""
def add(x,y):
    num = x[0] * y[1] + y[0] * x[1]
    den = x[1] * y[1]
    fraction = (num,den)
    if fraction[0] == fraction[1]: #Check to see if fraction simplifies to 1
        fraction = 1
        return fraction
    else:
        return fraction


def mult(x,y):
    num = x[0] * y[0]
    den = x[1] * y[1]
    fraction = (num,den)
    if fraction[0] == fraction[1]: #Check to see if fraction simplifies to 1
        fraction = 1
        return fraction
    else:
        return fraction
# Main
x = (1,2)
y = (1,2)
print(add(x,y))
print(mult(x,y))