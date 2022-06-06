from Warrior import Warrior


if __name__ == '__main__':

    playing = Warrior.game()

    if playing in ('Y', 'y'):
        print('Играем снова!')
        playing = Warrior.game()
    if playing in ('N', 'n'):
        print('Спасибо за игру!')
