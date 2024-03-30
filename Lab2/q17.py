# (a)
# Prompt for user input for height and weight
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
# Initialise a variable and assign the value that creates the user's BMI
bmi = weight / (height*height)
print(bmi)
print(" ")
# (b)
# Again prompt for user input but use different metrics this time
w = float(input("Enter your weight in pounds: "))
h = float(input("Enter your height in inches: "))
# Print the values before the conversion
print(w, "lbs")
print(h, "in")
# Initialise two variables to convert pounds to kilograms and inches to cm.
wkg = w * 0.45359237
hm = h * 2.54
# Print the converted values
print("The converted height and weight is as follows: ")
print(wkg, "kg")
print(hm, "cm")


