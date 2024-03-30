class Hero(object):
    """Basic template for hero. Contains name, power level, and health
    points attributes. Implements the punch method and string method."""

    def __init__(self, name="", power_level=1, health_points=100):
        self.name = name
        self.power_level = power_level
        self.health_points = health_points

    def punch(self) -> int:
        """Return the punch power, which is 2 times the hero's level"""
        return self.power_level * 2

    def __str__(self):
        """
        Return strings with attributes for the hero
        """
        hero_info = f"Name: {self.name}\n"
        hero_info += f"Power level: {self.power_level}\n"
        hero_info += f"Health points: {self.health_points}\n"
        return hero_info

class Archetype(Hero):
    """Basic template for archetype hero. Contains name, power level,health
    points and strike attributes. Implements the attack method, defence method
    combat method and string method."""

    def __init__(self, name="", power_level=1, health_points=100, strike=1):
        super().__init__(name, power_level, health_points)
        self.strike = strike

    def attack(self): # Returns the strikes power
        return self.strike * 3

    def defence(self):
        self.health_points += 10
        return self.health_points

    def combat(self, monster):
        """Simulating combat between the hero and a monster."""
        if not isinstance(monster, Monster): # Checks to see if there is two instances of the class Monster. 
            print("The hero only fights monsters and/or there has to be 2 monsters.")
            return False

        while self.health_points > 0 and monster.health_points > 0:
            # Heroes turn to attack
            monster.health_points -= self.punch() 
            print(f"{self.name} attacks {monster.name}. {monster.name}'s health: {monster.health_points}")

            # A check to see if the monster is defeated
            if monster.health_points <= 0:
                print(f"{self.name} wins! {monster.name} has been defeated.")
                return True

            # Monsters turn to attack
            self.health_points -= monster.attack()
            print(f"{monster.name} counterattacks. {self.name}'s health: {self.health_points}")

            # A check to see if the hero is defeated
            if self.health_points <= 0:
                print(f"{monster.name} wins! {self.name} has been defeated.")
                return False

        # Combat ended without a clear winner
        return False
    
    def __str__(self):
        """
        Return strings with attributes for the archetype hero
        """
        return f"Hero: \n" \
               f"Name: {self.name}\n" \
               f"Power level: {self.power_level}\n" \
               f"Health points: {self.health_points}\n" \
               f"Strike: {self.strike}\n" \
        
class Monster(object):
    def __init__(self, name, strength, health_points, roar, defense_points=0):
        self.name = name
        self.strength = strength
        self.health_points = health_points
        self.roar = roar
        self.defense_points = defense_points
        print(self.roar)
    
    def attack(self):
        return self.strength
    
    def defend(self):
        self.health_points += self.defense_points
        return self.health_points

    def __add__(self, other):
        if isinstance(other, Monster):
            # Concatenating roars and adding three exclamation marks
            new_roar = f"{self.roar} {other.roar}!!!"
            # Calculating combined strength and health_points
            combined_strength = self.strength + other.strength
            combined_health_points = self.health_points + other.health_points
            # Creating a new Monster with the combined attributes
            return Monster(name=f"{self.name} {other.name}", strength=combined_strength, health_points=combined_health_points, roar=new_roar)
        else:
            raise ValueError("Can only add two Monster instances")
        
    def __str__(self):
        """
        Returning strings with attributes for the monster
        """

        return f"Monster: \n" \
               f"Name: {self.name}\n" \
               f"Strength: {self.strength}\n" \
               f"Health points: {self.health_points}\n" \
               f"Defense points: {self.defense_points}\n" \


# Main scope
# Creating an instance of the Hero class
hero = Archetype(name="Knight", power_level=5, health_points=150, strike=2)
print(hero)

# Creating 2 instances of Monster using the Monster constructor
monster1 = Monster(name="Dragon", strength=8, health_points=120, roar="Roarrrrrrr")
print(monster1)
monster2 = Monster(name="Goblin", strength=4, health_points=80, roar="Roarrrrrrrrrrrrrr")
print(monster2)

# Creating a third instance of Monster by adding the first two monsters
combined_monster = monster1 + monster2
print(combined_monster)

# Making the hero combat each monster one at a time
for monster in [monster1, monster2, combined_monster]:
    if hero.combat(monster):
        print(f"{hero.name} emerges victorious!\n")
    else:
        print(f"{hero.name} has been defeated.\n")
