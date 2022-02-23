import random
from re import L
import time
from threading import Event
import sys
from time import sleep



words = '''       _            _         _____              
      | |          | |       |  __ \             
      | | ___      | | ___   | |__) |_ __   __ _ 
  _   | |/ _ \ _   | |/ _ \  |  _  /| '_ \ / _` |
 | |__| | (_) | |__| | (_) | | | \ \| |_) | (_| |
  \____/ \___/ \____/ \___/  |_|  \_\ .__/ \__, |
                                    | |     __/ |
                                    |_|    |___/ 
                                   
                                   © Fang 2022 \n'''
for char in words:
                sleep(0.0001)
                sys.stdout.write(char)
                sys.stdout.flush()

words = "A text-based JoJo rpg game by Fang \n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()




rand = random.randrange(1, 9)

class Star_Platinum(object):
    maxhealth = 200
    power = 90
    speed = 30
    health = maxhealth
    ability = "Star Platinum: Za Warudo (stops time for 3 seconds), Ora Ora Ora (80 dmg)"
    def use_ability(self):
        ab_num = input("Which ability would you like to use? (1/2): ")
        if ab_num == "1":
            print("You stopped time and attack the enemy!")
            ab_dmg = random.randrange(70, 100)
            Za_Hando.health = Za_Hando.health - ab_dmg
            print("The enemy's health is now", Za_Hando.health)
        elif ab_num == "2":
            print("You barraged the enemy with your punches!")
            Za_Hando.health = Za_Hando.health - 80
            print("The enemy's health is now", Za_Hando.health)
        else:
            print("Input either 1 or 2")

    def attack(self):
        dmg = Star_Platinum.power / rand
        Za_Hando.health = Za_Hando.health - dmg 
        print("The enemy took a hit. His health is now:", Za_Hando.health)


class The_World(object):
    maxhealth = 180
    power = 80
    speed = 30
    health = maxhealth
    def use_ability(self):
        input("Which ability would you like to use? (1/2)")
        if input == "1":
            print("You stopped time and attack the enemy!")
            ab_dmg = random.randrange(90, 120)
            Za_Hando.health = Za_Hando.health - ab_dmg
            print("The enemy's health is now", Za_Hando.health)
        elif input == "2":
            print("You barraged the enemy with your punches!")
            Za_Hando.health = Za_Hando.health - 80
            print("The enemy's health is now", Za_Hando.health)
        else:
            print("Input either 1 or 2")
    ability = "Za Warudo (stops time for 6 seconds), Muda Muda Muda (80 dmg)"
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
    def use_ability(self):
        input("Which ability would you like to use? (1)")
        if input == "1":
            print("You healed yourself!")
            print("Your health is now", user_stand.health + 60)
        else:
            print("Input either 1 or 2")
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
    def use_ability(self):
        input("Which ability would you like to use? (1)")
        if input == "1":
            print("YOu skipped time and attacked the enemy!")
            ab_dmg = random.randrange(80, 100)
            Za_Hando.health = Za_Hando.health - ab_dmg
            print("The enemy's health is now", Za_Hando.health)
        else:
            print("Input either 1 or 2")
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
        words = '''You have chosen Star Platinum.
        Your stats are: maxhealth = 200
        power = 90
        speed = 30
        ability = "Star Platinum: Za Warudo (stops time for 3 seconds), Ora Ora Ora (150 dmg)"'''
        for char in words:
            sleep(0.02)
            sys.stdout.write(char)
            sys.stdout.flush()
        break

    elif user_stand == 2:
        user_stand = The_World()
        words = '''You have chose The World.
        Your stats are: maxhealth = 180
        power = 80
        speed = 30
        ability = "Za Warudo (stops time for 6 seconds), Muda Muda Muda (150 dmg)"'''
        for char in words:
            sleep(0.02)
            sys.stdout.write(char)
            sys.stdout.flush()
        break

    elif user_stand == 3:
        user_stand = Golden_Experience()
        words = '''You have chose Golden Experience.
        Your stats are: maxhealth = 120
        power = 60
        speed = 50
        ability = "Self Heal (+60 health)"'''
        for char in words:
            sleep(0.02)
            sys.stdout.write(char)
            sys.stdout.flush()
        break

    elif user_stand == 4:
        user_stand = King_Crimson
        words = '''You have chose King Crimson.
        Your stats are: maxhealth = 100
        power = 85
        speed = 20
        ability = "Time Skip (skips 5 second)"'''
        for char in words:
            sleep(0.02)
            sys.stdout.write(char)
            sys.stdout.flush()
        break

    else:
        words = "Enter a valid number."
        for char in words:
            sleep(0.02)
            sys.stdout.write(char)
            sys.stdout.flush()
        continue

period()
period()
def pause():
    Event().wait(0.5)
    print (".")

words = "You're walking in the streets of Morioh Town \n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

def choose_passive():
    while True:

        choice = int(input('''What are you going to do?
        1. Attack 
        2. Stats
        3. Run
        4. Ability
        5. Inventory
        6. Quests
        7. Explore \n'''))

        if choice == 1:
            words = "There's no one to attack"
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 2:
            print("hp:", user_stand.maxhealth)
            print("power:", user_stand.power)
            print("speed:", user_stand.speed)
            period()
            continue

        elif choice == 3:
            words = "There's no one to run away from"
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 4:
            words = "Your ability:", user_stand.ability
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 5:
            words = "There's nothing in your possession."
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 6:
            words = "There are no quests, currently."
            for char in words:
                sleep(0.01)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 7:
            period()
            period()
            words = "You go and explore the town. \n"
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            Event().wait(1)
            words = '''You come across a strange house. You slowly walk in, there's a strange noise 
you look around to see a weird person, he attacks you!'''
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            pause(); pause(); pause()
            break

        else:
            words = "Choose a valid option!"
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

choose_passive()
        
words = '''The opponent uses his stand Za Hando
His stats are: Health: 100
Attack: 50
Speed: 20 \n'''
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()


while True:
        choice = int(input('''What are you going to do?
        1. Attack 
        2. Stats
        3. Run
        4. Ability
        5. Inventory
        6. Quests
        7. Explore \n'''))


        if Za_Hando.health <= 0:
            break

        if user_stand.health <= 0:
            break
        
        Za_Hando.attack(user_stand)


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
            Za_Hando.attack(user_stand)
            period()
            continue

        elif choice == 4:
            print("Your ability:", user_stand.ability)
            use_ab = input("Do you want to use your ability? (y/n): ")
            if use_ab == "y":
                user_stand.use_ability()
            elif use_ab == "n":
                continue
            else:
                print("Answer in y or n.")
                continue

            period()
            

        elif choice == 5:
            words = "There's nothing in your possession."
            for char in words:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 6:
            words = "There are no quests, currently."
            for char in words:
                sleep(0.01)
                sys.stdout.write(char)
                sys.stdout.flush()
            period()
            continue

        elif choice == 7:
            words = "You can't do that now!" 
            for char in words:
                sleep(0.01)
                sys.stdout.write(char)
                sys.stdout.flush() 
            continue

            

        else:
            words = "Choose a valid option!"
            for char in words:
                sleep(0.01)
                sys.stdout.write(char)
                sys.stdout.flush() 
            period()
            continue

if user_stand.health > 0:

    words = "You have successfully defeated Za Hando and the Enemy User! \n"
    for char in words:
                sleep(0.01)
                sys.stdout.write(char)
                sys.stdout.flush()

if Za_Hando.health > 0:
    words = "The enemy defeated you! Better Luck Next Time! \n"
    for char in words:
                sleep(0.01)
                sys.stdout.write(char)
                sys.stdout.flush()



words = "Well that's it for the game right now, cya idiots later!!!!!!!!!!!!!!!"
for char in words:
            sleep(0.09)
            sys.stdout.write(char)
            sys.stdout.flush()






















