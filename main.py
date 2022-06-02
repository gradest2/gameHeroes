from Warrior import *


if __name__ == '__main__':

    while 1:
        try:
            Warrior1, Warrior2, Warrior1_count, Warrior2_count = Warrior.start()
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            break
        Warrior.battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count)

        playing = input("Повторим?(Y/n)")
        if playing == "Y" or playing == "y":
            print('Играем снова!')
        if playing == "N" or playing == "n":
            break
        else:
            print("Чо ты ввел? Ах так, придется играть по новой.")


#Ввести в игру стоимость воина и деньги
#Ввести в игру противника, покупающего рандомно стеки
#Рефакторинг кода
