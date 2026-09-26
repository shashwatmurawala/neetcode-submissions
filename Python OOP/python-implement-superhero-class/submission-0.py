class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
bat = SuperHero("Batman", "Intelligence", 100)
sup = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(bat.name)
print(bat.power)
print(bat.health)
print(sup.name)
print(sup.power)
print(sup.health)