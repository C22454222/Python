# Q1
x = int(input("Enter a mark between 0-100: "))
if x >= 40:
  print("This is a pass mark")
elif x <40 and x >= 0:
  print("This is a fail")
else:
  print("Incorrect input")
print()
# Q2
x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))

if x > y:
  print(x,"is greater than", y)
elif y > x:
  print(x,"is smaller than", y)
elif x == y:
  print(x,"is equal to",y)
else:
  print("Wrong input")
print()
#Q3
x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))
z = input("Enter a symbol(+-*/): ")
if z == '+':
  print(x+y)
elif z == '-':
  print(x-y)
elif z == '*':
  print(x*y)
elif z == '/':
  print(x/y)
else:
  print("Wrong input")
print()

# 4
x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))
z = int(input("Enter an integer: "))

if x > y and x > z:
  print(x,"is the biggest")
elif y > x and y > z:
  print(y, "is the biggest")
elif z > x and z > y:
  print(z," is the biggest")
else:
  print("The numbers all equal each other or the input is wrong")
print()
