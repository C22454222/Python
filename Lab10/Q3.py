class Meeting(object):
    def __init__(self, people = 1):
        self.people = people

    def add(self, number=0):
        self.people += number
        return self.people

    def dec(self, number):
        self.people -= number
        return self.people
    
    def __str__(self):
        return f"Welcome. The current number of people in this meeting: {self.people}"

# Create an instance of the meeting class
meeting1 = Meeting(100)

# Call the 'add' method on the instance
meeting1.add(10)

meeting1.dec(5)

# Display the current number of people after adding
print(f"The current number of people in this meeting: {meeting1.people}")
