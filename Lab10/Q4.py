class member:
    def __init__(self,memberId,name):
        self.memberId = memberId
        self.name = name

    def __str__(self):
        return f"Member Id: {self.memberId}, Name: {self.name}"
    
class equipment:
    def __init__(self,equipmentId, name, quantity = 1):
        self.equipmentId = equipmentId
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Equipment Id: {self.equipmentId}, Name: {self.name} Quantity: {self.quantity}"
    
class gym:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.equipment = []

    def addMember(self, member):
        self.members.append(member)
    
    def addEquipment(self, equipment):
        self.equipment.append(equipment)

    def display(self):
        print(f"Members of {self.name} Gym: ")
        for member in self.members:
            print(member)

        print(f"Equipment in {self.name} Gym: ")
        for equipment in self.equipment:
            print(equipment)

member1 = member(1,"Chris")
member2 = member(2, "John")

equipment1 = equipment(1, "Treadmill", 10)
equipment2 = equipment(2, "Weights", 100)

gym1 = gym("Fitzone")

gym1.addMember(member1)
gym1.addMember(member2)
gym1.addEquipment(equipment1)
gym1.addEquipment(equipment2)

gym1.display()
                 
    


    
