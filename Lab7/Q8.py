my_dict = {'a': 15, 'c': 35, 'b': 20}

# (a) Print all the keys
print("Keys:", list(my_dict.keys()))

# (b) Print all the values
print("Values:", list(my_dict.values()))

# (c) Print all the keys and values pairs
print("Key-Value Pairs:", list(my_dict.items()))

# (d) Print all the keys and values pairs in order of key
print("Key-Value Pairs in Order of Key:", sorted(my_dict.items()))

# (e) Print all the keys and values pairs in order of value
print("Key-Value Pairs in Order of Value:", sorted(my_dict.items(), key=lambda x: x[1]))
