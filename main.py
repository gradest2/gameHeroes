from Warrior import *

def start():

    d = {'1': 'Goblin', '2' : 'Knight', '3' : 'Dragon', '4' : 'Ork'}

    print ("Начнется бой!")
    print("Выбери воинов, которые будут сражаться!")
    print("1: Goblin, 2: Knight, 3: Dragon, 4: Ork")
    Warrior1 = (input("Выбери первого воина: "))
    Warrior2 = (input("Выбери второго воина: "))

    if Warrior1 in d:
        Warrior1 = d.get(Warrior1)

    if Warrior2 in d:
        Warrior2 = d.get(Warrior2)

    return Warrior1, Warrior2


def mapping(Warrior1, Warrior2):
    Unit1 = Warrior("Goblin", 30, 5, 2)
    Unit2 = Warrior("Knight", 35, 10, 4)
    Unit3 = Warrior("Dragon", 200, 25, 20)
    Unit4 = Warrior("Ork", 33, 6, 7)

    if Warrior1 == "Goblin":
        Warrior1 = Unit1
    if Warrior1 == "Knight":
        Warrior1 = Unit2
    if Warrior1 == "Dragon":
        Warrior1 = Unit3
    if Warrior1 == "Ork":
        Warrior1 = Unit4

    if Warrior2 == "Goblin":
        Warrior2 = Unit1
    if Warrior2 == "Knight":
        Warrior2 = Unit2
    if Warrior2 == "Dragon":
        Warrior2 = Unit3
    if Warrior2 == "Ork":
        Warrior2 = Unit4

    return Warrior1, Warrior2


def battle(Warrior1, Warrior2):
    while Warrior1.health > 0 or Warrior2.health > 0:
        damage = Warrior2.attack - Warrior1.defense
        if damage > 0:
            Warrior1.health = Warrior1.health - damage
        print ("Атакует ", Warrior2.name, "| ", Warrior1.name, "health = ", Warrior1.health)
        if Warrior.check_helth(Warrior1.health):
            print (Warrior2.name, " победил!")
            break

        damage = Warrior1.attack - Warrior2.defense
        if damage > 0:
            Warrior2.health = Warrior2.health - damage
        print ("Атакует ", Warrior1.name, "| ", Warrior2.name, "health = ", Warrior2.health)
        if Warrior.check_helth(Warrior2.health):
            print (Warrior1.name, " победил!")
            break

Warrior1, Warrior2 = start()
Warrior1, Warrior2 = mapping(Warrior1, Warrior2)
print ("Сражаются: ", Warrior1.name, " против ", Warrior2.name)
battle(Warrior1, Warrior2)
