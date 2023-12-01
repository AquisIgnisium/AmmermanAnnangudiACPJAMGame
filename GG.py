import challenge
import os as os
import time as time
import random as rand
from random import shuffle
import string
def redeem_wordScramble(): 
    input("     You better redeem yourself right now")
    challenge_4 = challenge.wordScramble(1,30)
    if challenge_4 == 1:
        print("Giggles McSnickerdoodle:")
        input("     Close one but good job")
    elif challenge_4 == -1:
        print("Giggles McSnickerdoodle")
        input("     I would say you had a good run but I'd be lying, Bye!")
        os.system('cls')
        input("Womp Womp")
        quit()

def game(username):
    os.system('cls')
    print("Chief Patel:")
    input("     Good choice, I mean you should be able to do this without much struggle, I was hoping you would have picked a hard one")
    print("\n")
    print("How would you like to respond \nResponce 1:""Yeah lets just get this over with already.""\nResponce 2:""Lets sart out small what more can you tell me about the Giggle Gang""\nResponce 3:Well the other two sounded a little too dangerous and I want to have some fun")
    speaking_choice1 = input(">>")
    if speaking_choice1 == "1":
        print(username + ":")
        input("     Yea lets just get this over with already.")
        print("Chief Patel:")
        input("     Better going then")
    elif speaking_choice1 == "2":
        print(username + ":")
        input("     Lets start out small what more can you tell me about the Giggle Gang.")
        print("Chief Patel")
        input("     The Giggle Gang is a surprisingly serious group of criminals. They kidnap children and take away their happyness or ""giggles"". The group is led by Amy Schumer, the worst comedian in my opinion, but that does not matter right now. I need you to go infiltrate them and take Schumer down. Good luck I hope to see you back soon.")
    elif  speaking_choice1 == "3":
        print(username + ":")
        input("     Well the other two sounded a little too dangerous and I want to have some fun.")
        print("Chief Patel:")
        input("     Thats understandable but be warned their crimes are not for the light hearted and their leader is incredibly annoying.")
    print("One last thing before you leave, whats your undercover name")
    undercover_username = input(">>")
    os.system('cls')
    print("Giggles McSnickerdoodle (Giggle Gang Grunt):")
    input("     Get up, its time to get to work, since todays your first day were making you kidnap a few children, most people dont make it through the first day.")
    print("\n")
    print("Choose a responce \nResponce 1:""I wont let you down.""\nRespoce 2:""Already!?""\nResponce 3:Stay silent")
    speaking_choice2 = input(">>")
    if speaking_choice2 == "1":
        print(undercover_username + ":")
        input("     I wont let you down.")
    elif speaking_choice2 == "2":
        print(undercover_username + ":")
        input("     Already!?")
    elif speaking_choice2 == "3":
        print("\n\n")
    input("Complete this mini game to kidnap your first victim")
    challenge_1 = challenge.dnaBases(2,20)
    if challenge_1 == 1:
        print("Giggles McSnickerdoodle:")
        input("     One down two more to go.")
        input("\nComplete these two more challenges to finish your task")
        challenge_2 = challenge.closebrackets(1,15)
        if challenge_2 == 1:
            challenge_3 = challenge.retype(2,25)
            if challenge_3 == 1:
                print("Giggle McSnickerdoodle:")
                input("     Nice job! It looks like you have a good future in this group")
            elif challenge_3 == -1:
                print("Giggle McSnickerdoodle:")
                input("     So dissapointing, I almost thought you had potential")
                redeem_wordScramble()
        elif challenge_2 == -1:
            print("Giggle McSnickerdoodle:")
            input("     You almost made it, I'm not mad, just dissapionted")
            redeem_wordScramble()
    elif challenge_1 == -1:
            print("Giggle McSnickerdoodle:")
            input("     That was a very poor showing you better get your act together soon")
            redeem_wordScramble()
    input("     Since you were able to complete that task were gonna send you on a mission with some of our other grunts.\nMeet Vinnie ""The Giggler"" Gambino our Co Leader.")
    print("Vinnie ""The Giggler"" Gambino:")
    input("     Tommorow we take down a whole preschool, we are gonna kidnap every single child, meet here at 6:00 am tomorrow morning\n\n" + undercover_username + " follow me I'll take to your room")
    input("\n*You enter your room, a bright and colorful clown themed bedroom filled with mirrors, you lay down in the yellow clown car bed surprised you fit and drift off to sleep*")
    os.system('cls')
