import random
from re import L
import time
from threading import Event



print('''       _            _         _____              
      | |          | |       |  __ \             
      | | ___      | | ___   | |__) |_ __   __ _ 
  _   | |/ _ \ _   | |/ _ \  |  _  /| '_ \ / _` |
 | |__| | (_) | |__| | (_) | | | \ \| |_) | (_| |
  \____/ \___/ \____/ \___/  |_|  \_\ .__/ \__, |
                                    | |     __/ |
                                    |_|    |___/ 
                                   
                                   © Fang 2022''')

print("A text-based JoJo rpg game by Fang \n")


rand = random.randrange(9)

class Star_Platinum(object):
    maxhealth = 200
    power = 90
    speed = 30
    health = maxhealth
    ability = "Star Platinum: Za Warudo (stops time for 3 seconds), Ora Ora Ora (150 dmg)"
    def attack(self):
        dmg = Star_Platinum.power / rand
        Za_Hando.health = Za_Hando.health - dmg 
        print("The enemy took a hit. His health is now:", Za_Hando.health)


class The_World(object):
    maxhealth = 180
    power = 80
    speed = 30
    health = maxhealth
    ability = "Za Warudo (stops time for 6 seconds), Muda Muda Muda (150 dmg)"
    def attack(self):
        dmg = The_World.power / rand
        Za_Hando.health = Za_Hando.health - dmg
        print("The enemy took a hit. His health is now:", Za_Hando.health)

class Golden_Experience(object):
    maxhealth = 120
    power = 60
    speed = 50
    health = maxhealth
    ability = "Self Heal (+60 health)"
    def attack(self):
        dmg = Golden_Experience.power / rand
        Za_Hando.health = Za_Hando.health - dmg
        print("The enemy took a hit. His health is now:", Za_Hando.health)

class King_Crimson(object):
    maxhealth = 100
    power = 85
    speed = 20
    health = maxhealth
    ability = "Time Skip (skips 5 second)"
    def attack(self):
        dmg = King_Crimson.power / rand
        Za_Hando.health = Za_Hando.health - dmg
        print("The enemy took a hit. His health is now:", Za_Hando.health)

class Za_Hando(object):
    maxhealth = 100
    power = 50
    speed = 20
    health = maxhealth
    def attack(self):
        dmg = Za_Hando.power / rand
        user_stand.health = user_stand.health - dmg
        print("The user took a hit. Your health is now:", user_stand.health)


def period():
    Event().wait(0.5)
    print (". \n")

period(); period(); period(); period(); period()

Event().wait(1)
user_stand = int(input('''Choose a stand:
1. Star Platinum
2. The World
3. Golden Experience
4. King Crimson \n'''))

while True:
    if user_stand == 1:
        user_stand = Star_Platinum()
        print('''You have chosen Star Platinum.
        Your stats are: maxhealth = 200
        power = 90
        speed = 30
        ability = "Star Platinum: Za Warudo (stops time for 3 seconds), Ora Ora Ora (150 dmg)"''')
        break

    elif user_stand == 2:
        user_stand = The_World()
        print('''You have chose The World.
        Your stats are: maxhealth = 180
        power = 80
        speed = 30
        ability = "Za Warudo (stops time for 6 seconds), Muda Muda Muda (150 dmg)"''')
        break

    elif user_stand == 3:
        user_stand = Golden_Experience()
        print('''You have chose Golden Experience.
        Your stats are: maxhealth = 120
        power = 60
        speed = 50
        ability = "Self Heal (+60 health)"''')
        break

    elif user_stand == 4:
        user_stand = King_Crimson
        print('''You have chose King Crimson.
        Your stats are: maxhealth = 100
        power = 85
        speed = 20
        ability = "Time Skip (skips 5 second)"''')
        break

    else:
        ("Enter a valid number.")
        continue

period()
period()
def pause():
    Event().wait(0.5)
    print (".")

print("You're walking in the streets of Morioh Town")

def choose_passive():
    while True:

        choice = int(input(print('''What are you going to do?
        1. Attack 
        2. Stats
        3. Run
        4. Ability
        5. Inventory
        6. Quests
        7. Explore \n''')))

        if choice == 1:
            print("There's no one to attack")
            period()
            continue

        elif choice == 2:
            print("hp:", user_stand.maxhealth)
            print("power:", user_stand.power)
            print("speed:", user_stand.speed)
            period()
            continue

        elif choice == 3:
            print("There's no one to run away from")
            period()
            continue

        elif choice == 4:
            print("Your ability:", user_stand.ability)
            period()
            continue

        elif choice == 5:
            print("There's nothing in your possession.")
            period()
            continue

        elif choice == 6:
            print("There are no quests, currently.")
            period()
            continue

        elif choice == 7:
            period()
            period()
            print("You go and explore the town.")
            Event().wait(1)
            print("You come across a strange house")
            print('''You slowly walk in, there's a strange noise 
    you look around to see a weird person, he attacks you!''')
            pause(); pause(); pause()
            break

        else:
            print("Choose a valid option!")
            period()
            continue

choose_passive()
        
print('''The opponent uses his stand Za Hando
His stats are: Health: 100
Attack: 50
Speed: 20''')


while Za_Hando.health > 0:
        choice = int(input(print('''What are you going to do?
        1. Attack 
        2. Stats
        3. Run
        4. Ability
        5. Inventory
        6. Quests
        7. Explore \n''')))

        if choice == 1:
            user_stand.attack()
           
        elif choice == 2:
            print("hp:", user_stand.health)
            print("power:", user_stand.power)
            print("speed:", user_stand.speed)
            period()
            continue

        elif choice == 3:
            print("Tried to run away but failed.")
            Za_Hando.attack()
            period()
            continue

        elif choice == 4:
            print("Your ability:", user_stand.ability)
            use_ab = input(print("Do you want to use your ability? (y/n): ")).lower.strip
            if use_ab == "y":
                pass
            elif use_ab == "n":
                continue
            else:
                print("Answer in y or n.")
                continue

            period()
            

        elif choice == 5:
            print("There's nothing in your possession.")
            period()
            continue

        elif choice == 6:
            print("There are no quests, currently.")
            period()
            continue
            

        elif choice == 7:
            print("You can't do that now!")
            continue
            

        else:
            print("Choose a valid option!")
            period()
            continue

print("You have successfully defeated Za Hando and the Enemy User!")






















        
        
















