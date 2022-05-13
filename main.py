from Warrior import *


Warrior1, Warrior2, Warrior1_count, Warrior2_count = Warrior.start()
Warrior1, Warrior2 = Warrior.mapping(Warrior1, Warrior2)
print ("Сражаются: ", Warrior1.name, "в количестве: ", Warrior1_count, "против ", Warrior2.name, "в количестве: ", Warrior2_count)
Warrior.battle(Warrior1, Warrior2, Warrior1_count, Warrior2_count)


#больше типов юнитов
#немного графики
