''' 
    Name: Snowball-Mania
    Author: Ryker McCombe
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.11.9
'''
import time 

import random
def main():
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name?  ")
    opponent = input("Great to have you here, " + name + "! Who do you want to play agianst?  ")
    print(name + " vs. " + opponent)

    players = []
    players.append(name)
    players.append(opponent)

    nextPlayer = ""

    while (nextPlayer != "DONE"):
        nextPlayer = input("Are there any more opponents? IF so, type them one at a time (or DONE) and press 'Enter'. ")
        players.append(nextPlayer)
    players.remove("DONE")

    choice = input("Do you want to choose who you throw the snowball at or do you want it to be random? (Type yes or no)  ")

    gameplay(name, players, choice)

    

def gameplay(name, players, manual):
    # randomly choose one person to throw a snoball at the other
    while (len(players)>1):
        thrower = random.choice(players)
        if (thrower == name):
            if (manual == "yes"):       #Manual Mode
                target = input("You are up! Who do you want to throw the snowball at?   ")
            else:       # Auto mode
                #print(thrower)
                target = random.choice(players)
                while (target == thrower):
                    target = random.choice(players)
                #print(target)
        else:       # thrower is not us, so pick someone randomly
                #print(thrower)
                target = random.choice(players)
                while (target == thrower):
                    target = random.choice(players)
                #print(target)
        print(thrower + " is throwing a snowball " + target + "!")
        # generate a random number touse as the hitNum
        time.sleep(2)
        hitNum = random.randint(1, 5)
        success = hitResult(hitNum)
        if (success == True):
            print("It's a hit! " + target + " is down!")
            if name == thrower:
                name = input("Do you have anything to say after that beast of a shot? If not hit 'Enter'  ")
            players.remove(target)
        else:
            print("Unfortunately, " + thrower + " has very bad aim and missed.")
            if target == name and success == False:
                target = input("Do you have anything to say to them? If not hit 'Enter'  " )

                

    print(players[0] + " is the best snowballer in all the land!!!")


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum == 3):     #1 in 5 chance... I chose 3
        return True
    return False

main()
