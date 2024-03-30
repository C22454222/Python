#Q7
i = 999
count = 0
while i >= 100:

  if i % 17 == 0:
    print(i)
    count+=1
  i-=1
print()
print("The amount of numbers that divide into 17 evenly",count)