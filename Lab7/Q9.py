d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Create an empty dictionary to store the combined values
d3 = {}

# Add values from d1 to d3
for key, value in d1.items():
    d3[key] = value + d3.get(key, 0)

# Add values from d2 to d3
for key, value in d2.items():
    d3[key] = value + d3.get(key, 0)

# Print the result
print("Combined Dictionary:", d3)
