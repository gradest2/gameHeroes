from Warrior import *

print("Эта игра сделает меня триллионером!")

while 1:
    try:
        Warrior1, Warrior2, Warrior1_count, Warrior2_count = Warrior.start()
    except ValueError or AttributeError:
        print("Ошибка при вводе данных, повторите попытку.")
        Warrior1, Warrior2, Warrior1_count, Warrior2_count = Warrior.start()

    Warrior1, Warrior2 = Warrior.mapping(Warrior1, Warrior2)
    print ("Сражаются: ", Warrior1.name, "в количестве: ", Warrior1_count, "против ", Warrior2.name, "в количестве: ", Warrior2_count)
    Warrior.battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count)

    playing = input("Повторим?(Y/n)")
    if playing == "Y" or playing == "y":
        print('Всё хорошо.')
    if playing == "N" or playing == "n":
        break
    else:
        print("Чо ты ввел? Ах так, придется играть по новой.")


#больше типов юнитов
#немного графики
