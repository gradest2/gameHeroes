import random, time
import yaml

class Warrior:
    """Class make unic unit"""
    def __init__(self, name, health, attack_min, attack_max, defense, price):
        self.name        = name
        self.health      = health
        self.attack_min  = attack_min
        self.attack_max  = attack_max
        self.defense     = defense
        self.price       = price

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
                           gameData["GameUnits"][Unit]["Defense"],
                           gameData["GameUnits"][Unit]["Price"])

        return Unit


    def check_user_army(max_user_army):
        Warrior1_count = int(input("Введите количество юнитов, которые хотите купить: " ))
        while Warrior1_count > max_user_army:
            print("У вас недостаточно золота на покупку. Вы можете купить максимум: ", max_user_army)
            Warrior1_count = int(input("Введите количество юнитов, которые хотите купить: " ))
        return Warrior1_count

    #Ввод пользователем данных о стеках
    def start():

        zoloto = 10000
        ai_zoloto = zoloto
        print ("Начнется бой!")
        print("Выбери воинов, которые будут сражаться! У Вас только ", zoloto, " золота")


        #Сформировать словарь и вывести сообщения выбора войск
        gameData = Warrior.config()
        dict = {}
        i = 1
        for k, v in gameData["GameUnits"].items():
            dict.update({i: k})
            print (i, ":", k)
            i += 1

        try:
            Warrior1 = Warrior.mapping(dict.get(int(input("Выбери свою армию: "))))
            max_user_army = zoloto//Warrior1.price
            print("Максимальное количество юнитов, которое вы можете купить: ",  max_user_army)
            Warrior1_count = Warrior.check_user_army(max_user_army)
            zoloto = zoloto - Warrior1_count * Warrior1.price

            #AI выбирает свою армию
            Warrior2 = Warrior.mapping(dict.get(int(random.randint(1, i-1))))
            max_ai_army = ai_zoloto//Warrior2.price
            Warrior2_count = max_ai_army
            print("Компьютер купил:", Warrior2.name, "В количестве: ",  max_ai_army)
            ai_zoloto = ai_zoloto - Warrior2_count * Warrior2.price
            time.sleep(3)
        except (ValueError, KeyError):
            print ("Введены неверные данные. Перезапустите игру и попробуйте снова!")
            return 1

        return Warrior1, Warrior2, Warrior1_count, Warrior2_count


    #Битва
    def battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count):

        print ("Сражается армия игрока", Warrior1_count, Warrior1.name, "против компьютера", Warrior2_count, Warrior2.name)
        #print ("Сражается игрок с", Warrior1.name, "в количестве:", Warrior1_count, "против компьютера с", Warrior2.name, "в количестве:", Warrior2_count)
        time.sleep(3)
        health_sum1 = Warrior1.health * Warrior1_count
        health_sum2 = Warrior2.health * Warrior2_count

        while Warrior1.health > 0 or Warrior2.health > 0:
            #Атака первого стека
            damage = Warrior.random_attack(Warrior1.attack_min, Warrior1.attack_max) * Warrior1_count - Warrior2.defense
            if damage > 0:
                health_sum2 = health_sum2 - damage
                Warrior2_count = int(health_sum2 / Warrior2.health) + 1
            print ("Атакует игрок", Warrior1.name, "| ", Warrior2.name, "осталось:", Warrior2_count)
            if Warrior.check_helth(health_sum2):
                print ("Вы победили!")
                break
            time.sleep(0.5)

            #Атака второго стека
            damage = Warrior.random_attack(Warrior2.attack_min, Warrior2.attack_max) * Warrior2_count - Warrior1.defense
            if damage > 0:
                health_sum1 = health_sum1 - damage
                Warrior1_count = int(health_sum1 / Warrior1.health) + 1
            print ("Атакует компьютер", Warrior2.name, "| ", Warrior1.name, "осталось:", Warrior1_count)
            if Warrior.check_helth(health_sum1):
                print ("Вы проиграли!")
                break
            time.sleep(0.5)
