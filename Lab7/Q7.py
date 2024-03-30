"""
7. Using list comprehension
(a) Generate a list of square numbers
(b) Convert a list of colors = ['Red', 'Blue', 'Green', 'Black', 'White'] to upper case
(c) Find all of the numbers from 1-1000 that are divisible by 7
(d) Find all of the numbers from 1-1000 that have a 3 in them
(e) Count the number of spaces in a string
(f) Remove all of the vowels in a string
(g) Find all of the words in a string that are less than 4 letters
(h) Challenge! Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9).
The first part is given below. You need to find out the second list comprehension
"""
# (a)
print([n**2 for n in range(1,11)])
# (b) 
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
print([n.upper() for n in colors])
# (c)
print([n for n in range(1,1001) if n % 7 == 0 ])  
# (d) 
print([n for n in range(1, 1001) if '3' in str(n)])
# (e) 
count_of_spaces = sum(1 for char in "Hi there" if char == ' ')
print(count_of_spaces)
# (f)
original_string = "Caeiout"
result_string = ''.join(char for char in original_string if char not in {'a', 'e', 'o', 'i', 'u'})
print(result_string)
# (g)
sentence = "This is a sample string with words of various lengths."

short_words = [word for word in sentence.split() if len(word) < 4]

print(short_words)
# (h)
divisible_numbers = [num for num in range(1, 1001) if any(num % digit == 0 for digit in range(2, 10))]

print(divisible_numbers)


