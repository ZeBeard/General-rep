import random as r
names = (
    "Achille Lauro", "Andrea Doria", "Argonaut", "Argus", "Beagle", "Bismarck",
    "Bounty", "Britannic", "Carpathia", "Charlotte Dundas", "Clermont",
    "Constitution", "Cutty Sark", "Dreadnought", "Eastland", "Enterprise",
    "Flying Dutchman", "Fulton", "Glomar Challenger", "Graf Spee", "Holland",
    "Hunley", "Kon-Tiki", "Lenin", "Long Beach", "Lusitania", "Mauretania",
    "Missouri", "Nautilus", "Olympic", "Queen Elizabeth", "Ra", "Santa Maria",
    "Titanic", "Triton", "Turtle", "Victoria III")

class Ship:
    """This class is a simulation of a ship"""

    def __init__(self, name, armor, power, team):
        """
        ship has following attributes:
        name
        armor
        power
        team
        timeTillSank - set to 2 at the start of the Battle
        """
        self.name = name
        self.armor = armor
        self.power = power
        self.team = team
        self.timeTillSank = 2

    def fire(self):
        """
        simulates ship firing a round and returns it damage value.
        damage is calculated as power * random float between 0.25 and 1
        """
        damage = round(self.power * r.uniform(0.25, 1), 2)
        # print(f"{self.name} shoots")
        return damage

    def takeDamage(self, damage):
        """
        simulates taking damage
        by taking damage reduction of armor is meant
        """
        self.armor -= damage
        # print(
        #     f'{self.name} had been hit for {damage} and left '
        #     f'with {round(self.armor, 2) if self.armor > 0 else "no"} armor')

    def cleanUp(self):
        """simulates a ship taking in water and going down
        if a ship has no armor its time till sink will go down
        by 1 point each turn
        """
        if self.armor <= 0:
            self.timeTillSank -= 1
            # print(f"{self.name} will sink in {self.timeTillSank}")