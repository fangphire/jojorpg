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

class Star_Platinum(object):
    health = 200
    power = 90
    speed = 30
    ability = "Star Platinum: Za Warudo (stops time for 3 seconds), Ora Ora Ora (150 dmg)"

class The_World(object):
    health = 180
    power = 80
    speed = 30
    ability = "Za Warudo (stops time for 6 seconds), Muda Muda Muda (150 dmg)"

class Golden_Experience(object):
    health = 120
    power = 60
    speed = 50
    ability = "Self Heal (+60 health)"

class King_Crimson(object):
    health = 100
    power = 85
    speed = 20
    ability = "Time Skip (skips 5 second)"

def period():
    Event().wait(0.5)
    print (". \n")

period()
period()
period()
period()
period()

Event().wait(1)
user_stand = int(input('''Choose a stand:
1. Star Platinum
2. The World
3. Golden Experience
4. King Crimson \n'''))

while True:
    if user_stand == 1:
        print('''You have chosen Star Platinum.
        Your stats are: health = 200
        power = 90
        speed = 30
        ability = "Star Platinum: Za Warudo (stops time for 3 seconds), Ora Ora Ora (150 dmg)"''')
        break

    elif user_stand == 2:
        print('''You have chose The World.
        Your stats are: health = 180
        power = 80
        speed = 30
        ability = "Za Warudo (stops time for 6 seconds), Muda Muda Muda (150 dmg)"''')
        break

    elif user_stand == 3:
        print('''You have chose Golden Experience.
        Your stats are: health = 120
        power = 60
        speed = 50
        ability = "Self Heal (+60 health)"''')
        break

    elif user_stand == 4:
        print('''You have chose King Crimson.
        Your stats are: health = 100
        power = 85
        speed = 20
        ability = "Time Skip (skips 5 second)"''')
        break

    else:
        ("Enter a valid number.")
        continue

period()
period()

def Attaack():
    pass

def Stats():
    pass

def Run():
    print("You tried to run away but failed!")

def Ability():
    pass

def Inventory():
    print("You have nothing in your possession.")

# print('''What are you going to do?
#  1. Attack 
#  2. Stats
#  3. Run
#  4. Ability
#  5. Inventory
#  6. Quests
#  7. Explore''')

print("You're walking in the streets of Morioh Town")
choice = input(print('''What are you going to do?
1. Attack 
2. Stats
3. Run
4. Ability
5. Inventory
6. Quests
7. Explore'''))
















