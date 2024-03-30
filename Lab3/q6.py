#6
#(a)
cigars = int(input("What are the number of cigars: "))
if cigars >= 40 and cigars <= 60:
  print("Party is a success")
elif cigars > 60:
  week = input("Is it the weekend(Y/N)? ")
  if week == 'Y':
    print("Party is a success")
  else:
    print("Party is not a success")
elif cigars < 40:
  print("Party is not a success")
else:
  print("Incorrect input")
print()
#(b)
temp = int(input("What is the temperature in celcius: "))
if temp >= 60 and temp <= 90:
  print("The squirrels play outside")
elif temp > 90 and temp <= 100:
  summer = input("Is it summer(Y/N)? ")
  if summer == 'Y':
    print("The squirrels play outside")
  else:
    print("The squirrels don't play outside")
elif temp < 60 or temp > 100:
  print("The squirrels don't play outside")
else:
  print("Wrong input")
print()
#(c)
def get_ticket(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2

# Get user input for speed and birthday
speed = int(input("Enter your speed: "))
is_birthday = input("Is it your birthday? (yes or no): ").lower() == "yes"

ticket_result = get_ticket(speed, is_birthday)

if ticket_result == 0:
    print("No ticket")
elif ticket_result == 1:
    print("Small ticket")
else:
    print("Big ticket")