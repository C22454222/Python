"""
6. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""

def sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j][1] < list[j+1][1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort(list))