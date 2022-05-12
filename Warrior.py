class Warrior:
    """Class make unic unit"""
    def __init__(self, name, health, attack, defense):
        self.name    = name
        self.health  = health
        self.attack  = attack
        self.defense = defense

    def check_helth(helth):
        if helth <=0:
            return 1
        else:
            return 0
