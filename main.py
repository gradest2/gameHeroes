from Warrior import *


if __name__ == '__main__':

    while 1:
        try:
            Warrior1, Warrior2, Warrior1_count, Warrior2_count = Warrior.start()
        except TypeError:
            break
        print ("Сражаются: ", Warrior1.name, "в количестве: ", Warrior1_count, "против ", Warrior2.name, "в количестве: ", Warrior2_count)
        Warrior.battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count)

        playing = input("Повторим?(Y/n)")
        if playing == "Y" or playing == "y":
            print('Играем снова!')
        if playing == "N" or playing == "n":
            break
        else:
            print("Чо ты ввел? Ах так, придется играть по новой.")
