#Q8(a)
# Part (a)
X = int(input("Enter an integer (X): "))
sum_of_consecutive_integers = 0
for i in range(1, X + 1):
    sum_of_consecutive_integers += i
print("Sum of", X, "consecutive integers starting at 1:", sum_of_consecutive_integers)

# Part (b)
for i in range(1, X + 1):
    sum_partial = 0
    for j in range(1, i + 1):
        sum_partial += j
    print("Sum of first", i, "consecutive integers:", sum_partial)

# Part (c)
for i in range(1, X + 1):
    sum_partial = 0
    for j in range(1, i + 1):
        sum_partial += j
    if sum_partial % i == 0:
        print("Sum of first", i, "consecutive integers:", sum_partial)
