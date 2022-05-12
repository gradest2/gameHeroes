from Warrior import *
import time


def start():

    dict = {'1': 'Goblin', '2' : 'Knight', '3' : 'Dragon', '4' : 'Ork'}

    print ("Начнется бой!")
    print("Выбери воинов, которые будут сражаться!")
    print("1: Goblin, 2: Knight, 3: Dragon, 4: Ork")

    Warrior1 = input("Выбери первую армию: ")
    Warrior1_count = int(input("Введите количество юнитов: " ))
    Warrior2 = input("Выбери вторую армию: ")
    Warrior2_count = int(input("Введите количество юнитов: " ))

    if Warrior1 in dict:
        Warrior1 = dict.get(Warrior1)

    if Warrior2 in dict:
        Warrior2 = dict.get(Warrior2)

    return Warrior1, Warrior2, Warrior1_count, Warrior2_count


def mapping(Warrior1, Warrior2):
    Unit1 = Warrior("Goblin", 7, 3, 1)
    Unit2 = Warrior("Knight", 15, 6, 3)
    Unit3 = Warrior("Dragon", 200, 100, 30)
    Unit4 = Warrior("Ork", 20, 7, 2)

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


def battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count):

    health_sum1 = Warrior1.health * Warrior1_count
    health_sum2 = Warrior2.health * Warrior2_count

    while Warrior1.health > 0 or Warrior2.health > 0:
        damage = Warrior1.attack * Warrior1_count - Warrior2.defense
        if damage > 0:
            health_sum2 = health_sum2 - damage
            Warrior2_count = int(health_sum2 / Warrior2.health) + 1
        print ("Атакует ", Warrior1.name, "| ", Warrior2.name, "осталось:", Warrior2_count, "с общим health = ", health_sum2)
        if Warrior.check_helth(health_sum2):
            print (Warrior1.name, " победил!")
            break
        time.sleep(0.5)

        damage = Warrior2.attack * Warrior2_count - Warrior1.defense
        if damage > 0:
            health_sum1 = health_sum1 - damage
            Warrior1_count = int(health_sum1 / Warrior1.health) + 1
        print ("Атакует ", Warrior2.name, "| ", Warrior1.name, "осталось:", Warrior1_count, "с общим health = ", health_sum1)
        if Warrior.check_helth(health_sum1):
            print (Warrior2.name, " победил!")
            break
        time.sleep(0.5)

Warrior1, Warrior2, Warrior1_count, Warrior2_count = start()
Warrior1, Warrior2 = mapping(Warrior1, Warrior2)
print ("Сражаются: ", Warrior1.name, "в количестве: ", Warrior1_count, "против ", Warrior2.name, "в количестве: ", Warrior2_count)
battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count)
