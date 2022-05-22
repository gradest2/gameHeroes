import random, time
import yaml

class Warrior:
    """Class make unic unit"""
    def __init__(self, name, health, attack_min, attack_max, defense):
        self.name        = name
        self.health      = health
        self.attack_min  = attack_min
        self.attack_max  = attack_max
        self.defense     = defense

    #Проверка жив или мертв стек
    def check_helth(helth):
        if helth <=0:
            return 1
        else:
            return 0


    #Случайная атака
    def random_attack(attack_min, attack_max):
        result = random.randint(attack_min, attack_max)
        return result


    #Чтение конфига
    def config():

        stream = open("data.yaml", 'r')
        gameData = yaml.safe_load(stream)
        return gameData

    #Маппинг данных
    def mapping(Unit):

        gameData = Warrior.config()

        Unit  = Warrior(gameData["GameUnits"][Unit]["Name"],
                           gameData["GameUnits"][Unit]["Health"],
                           gameData["GameUnits"][Unit]["Attack_min"],
                           gameData["GameUnits"][Unit]["Attack_max"],
                           gameData["GameUnits"][Unit]["Defense"])

        return Unit


    #Ввод пользователем данных о стеках
    def start():

        print ("Начнется бой!")
        print("Выбери воинов, которые будут сражаться!")

        #Сформировать словарь и вывести сообщения выбора войск
        gameData = Warrior.config()
        dict = {}
        i = 1
        for k, v in gameData["GameUnits"].items():
            dict.update({i: k})
            print (i, ":", k)
            i += 1

        try:
            Warrior1 = int(input("Выбери первую армию: "))
            Warrior1_count = int(input("Введите количество юнитов: " ))
            Warrior2 = int(input("Выбери вторую армию: "))
            Warrior2_count = int(input("Введите количество юнитов: " ))

            if Warrior1 in dict and Warrior2 in dict:
                Warrior1 = Warrior.mapping(dict.get(Warrior1))
                Warrior2 = Warrior.mapping(dict.get(Warrior2))
        except ValueError or KeyError:
            print ("Введены неверные данные. Перезапустите игру и попробуйте снова!")
            return 1

        return Warrior1, Warrior2, Warrior1_count, Warrior2_count


    #Битва
    def battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count):

        health_sum1 = Warrior1.health * Warrior1_count
        health_sum2 = Warrior2.health * Warrior2_count

        while Warrior1.health > 0 or Warrior2.health > 0:
            #Атака первого стека
            damage = Warrior.random_attack(Warrior1.attack_min, Warrior1.attack_max) * Warrior1_count - Warrior2.defense
            if damage > 0:
                health_sum2 = health_sum2 - damage
                Warrior2_count = int(health_sum2 / Warrior2.health) + 1
            print ("Атакует ", Warrior1.name, "| ", Warrior2.name, "осталось:", Warrior2_count, "с общим health = ", health_sum2)
            if Warrior.check_helth(health_sum2):
                print (Warrior1.name, " победил!")
                break
            time.sleep(0.5)

            #Атака второго стека
            damage = Warrior.random_attack(Warrior2.attack_min, Warrior2.attack_max) * Warrior2_count - Warrior1.defense
            if damage > 0:
                health_sum1 = health_sum1 - damage
                Warrior1_count = int(health_sum1 / Warrior1.health) + 1
            print ("Атакует ", Warrior2.name, "| ", Warrior1.name, "осталось:", Warrior1_count, "с общим health = ", health_sum1)
            if Warrior.check_helth(health_sum1):
                print (Warrior2.name, " победил!")
                break
            time.sleep(0.5)
