import challenge
import os as os
import time as time
import random as rand
from random import shuffle
import string
import sys
def print_slow(i):
    for m in i:
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.2)
def game(username):
    os.system('cls')
    print("Chief Patel:")
    input("    Interesting choice " + username)
    input("    I think that if you put your head down and attack this gang with all of your gang, you can win")
    input("    Before I send you off, what is your undercover name?")
    undercoverName = input(">>")
    os.system('cls')
    print("Julian Denburg (Black Diamond Grunt)")
    input("    Get up!")
    input("*You wake up to Julian holding a gun against your temple. His haircut is choppy and uneven*")
    input("Disarm the Gun!")
    userChallenge1 = challenge.closebrackets(3,10)
    if userChallenge1 == -1:
        print("Julian Denburg:")
        input("    Get up off the ground you nasty runt")
        input("    I see behavior like that again")
        input("    Your out!")
    else:
        print("Julian Denburg:")
        print("    I see you aren't as stupid and weak as I thought")
        print("    I don't ever want to see a failure from you")
    input("*Julian drags you off the bed*")
    print("Julian Denburg:")
    input("    Your first challenge comes up soon")
    input("    By soon I mean in 5 seconds")
    input("    Go down the stairs and cook perfect pancakes for the boss leader, Christopher Harloff")
    input("*You stumble down the stairs as you see a giant sitting at a one person dining table*")
    print_slow("Christopher Harloff:")
    input("\n    GET ME BREAKFAST BOY!")
    input("*You scramble around the kitchen making food*")
    input("Scramble the Eggs!")
    userChallenge2 = challenge.dnaBases(3,10)
    if userChallenge2 == -1:
        print("*Harloff rips your limbs off due to your failure*")
        input("*Julian says I told you so*")
        print("You Lose!")
        quit()
    input("Mix the Batter!")
    userChallenge3 = challenge.wordScramble(3,10)
    if userChallenge3 == -1:
        print("*Harloff rips your limbs off due to your failure*")
        input("*Julian says I told you so*")
        print("You Lose!")
        quit()
    input("Squeeze the Hash Browns!")
    userChallenge4 = challenge.arithmatic(11,15,"*")
    if userChallenge4 == -1:
        print("*Harloff rips your limbs off due to your failure*")
        input("*Julian says I told you so*")
        print("You Lose!")
        quit()
    print_slow("Christopher Harloff:")
    input("\n    WHERE IS THE FOOD")
    input("\n    I NEED FOOD")
    input("Grate the Cheese!")
    userChallenge5 = challenge.MemoryGame(4,10)
    if userChallenge5 == -1:
        print("*Harloff rips your limbs off due to your failure*")
        input("*Julian says I told you so*")
        print("You Lose!")
        quit()
    input("Plate the food!")
    userChallenge6 = challenge.retype(3,10)
    if userChallenge6 == -1:
        print("*Harloff rips your limbs off due to your failure*")
        input("*Julian says I told you so*")
        print("You Lose!")
        quit()
    print_slow("Christopher Harloff:")
    input("\n    THIS FOOD IS....")
    print_slow("\n    ACCEPTABLE")
    print("Julian Denburg:")
    input("    Sorry the food wasn't better boss")
    input("    Next time he does that...")
    input("    I'll kill him")
    input()