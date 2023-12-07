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
    print("Chief Sanjay Patel:")
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
    print("Vinny ""The Giggler"" Gambino:")
    input("     You ready to get going?")
    print("\nChoose a responce \nResponce 1:""Yea lets hit the road""\nRespoce 2:""Of course""\nResponce 3:""As I'll ever be")
    input(">>")
    print("Vinny ""The Giggler"" Gambino:")
    input("     Good lets get going")
    input("\n \n        Ok were here lets get in and get out make sure to get every last child in there")
    input("Quick pick the lock to get inside")
    challenge_5 = challenge.arithmatic(3,30,"+")
    if challenge_5 == 1:
        print("Vinnie ""The Giggler"" Gambino:")
        input("     Nice one")
    elif challenge_5 == -1:
        print("Vinnie ""The Giggler"" Gambino:")
        input("     It ain't matter")
        input("*Vinnie kicks down the door*")
    input("     Quick grab the kids")
    challenge_6 = challenge.MemoryGame(1,10)
    challenge_7 = challenge.dnaBases(2,20)
    challenge_8 = challenge.retype(2,20)
    challenge_9 = challenge.closebrackets(1,15)
    challenge_10 = challenge.wordScramble(1,30)
    if challenge_6 + challenge_7 + challenge_8 + challenge_9 + challenge_10 < 0:
        print("Vinny ""The Giggler"" Gambino:")
        input("     Come on " + undercover_username +" what was that, do better")
        input(" redeem your self right now")
        redeem_challenge_2 = challenge.arithmatic(5,30,"*")
        if redeem_challenge_2 == 1:
            print("Vinnie ""The Giggler"" Gambino:")
            input("     Good job maybe its time for you top meet our leader")
        elif redeem_challenge_2 == -1:
            print("Vinnie ""The Giggler"" Gambino:")
            input("     Thats really dissapionting I thought you coulda been one of the greats \nBye")
            quit()
    elif challenge_6 + challenge_7 + challenge_8 + challenge_9 + challenge_10 > 0:
        print("Vinny ""The Giggler"" Gambino:")
        input("     Good job " + undercover_username +" it might be time for you to meet the leader")
    input("     Tomorrow at noon meet me behind the clown house and I'll introduce you two, now lets get going back home")
    os.system("cls")
    print("Vinny The Giggler Gambino:")
    input("     There you are, it feels like I've been waiting forever we need to hurry")
    input("     This is a very special oppourtunity be thankful")
    input("     I present to you, drumroll please...")
    input("     Amy Schumer")
    print("\nHow would you like to introduce yourself\nResponce 1:Its nice to meet you\nResponce 2:Its such an honor and I'm so glad to be here\n*Look at her while sin city plays in the backgroung* (W rizz)")
    speaking_choice3 = input(">>")
    if speaking_choice3 == "1":
        print(undercover_username = ":")
        input("     Its nice to meet you")
    elif speaking_choice3 == "2":
        print(undercover_username + ":")
        input("     Its such an honor and I'm so glad to be here")
    elif speaking_choice3 == "3":
        print(undercover_username + ":")
        input("     *Look at her while sin city plays in the backgroung* (W rizz)")
    print("Amy Schumer:")
    input("     Why thank you")
    input("     I've heard so many good things about you from Vinny here")
    print(undercover_username)
    input("     Thats good to hear but just so you know I'm about to take you down")
    print("Amy Schumer:")
    input("     Thats to bad")
    input("     Take this")
    lose_count = 0
    score = 0
    responses = ["Here's anhother one" , "Take this" , "Stop while you still can" , "The kids didn't call me Amy Schumer; they called me Amy Jewmer.", "Speaking of things that should already be dead, Charlie Sheen is still alive!" , "I feel like such a lameo buying Plan B" , "I made out with a homeless guy by accident" , "In New York, I'm a six — a seven with all the padding. But in Miami, I was like a negative three", "Get back here", "Your so annoying" , "I'm a hot mess, but I'm a unique hot mess. I own it", "I used to have boyfriend standards, but now I just have snack requirements", "I like my coffee like I like my men; strong, dark, and rich in taste" , "I feel like all my best friends are cookies" , "I don't know if I'm getting any smarter, but I'm getting better at pretending to be smart"]
    while lose_count < 3 and score < 15:
        challenge_11 = challenge.arithmatic(2,20,"-")
        if challenge_11 == 1:
            score += 1
        elif challenge_11 == -1:
            lose_count += 1
        if lose_count == 3 or score == 15:
                break
        input("     " + rand.choice(responses))
        challenge_12 = challenge.wordScramble(1,30)
        if challenge_12 == 1:
            score += 1
        elif challenge_12 == -1:
            lose_count += 1
        if lose_count == 3 or score == 15:
                break
        input("     " + rand.choice(responses))
        challenge_13 = challenge.dnaBases(2,15)
        if challenge_13 == 1:
            score += 1
        elif challenge_13 == -1:
            lose_count += 1
        if lose_count == 3 or score == 15:
                break
        input("     " + rand.choice(responses))
        challenge_14 = challenge.closebrackets(1,20)
        if challenge_14 == 1:
            score += 1
        elif challenge_14 == -1:
            lose_count += 1
        if lose_count == 3 or score == 15:
                break
        input("     " + rand.choice(responses))
        challenge_15 = challenge.MemoryGame(1,10)
        if challenge_15 == 1:
            score += 1
        elif challenge_15 == -1:
            lose_count += 1
        if lose_count == 3 or score == 15:
                break
        input("     " + rand.choice(responses))
        challenge_16 = challenge.retype(2,15)
        if challenge_16 == 1:
            score += 1
        elif challenge_16 == -1:
            lose_count += 1
        if lose_count == 3 or score == 15:
                break
        input("     " + rand.choice(responses))
    if lose_count == 3:
        print("Amy Schumer:")
        input("     You really thougt that you could beat me, how funny")
        os.system("cls")
        print("Captain Sanjay Patel:")
        input("     hurry get him to the hospital, NOW")
        input("     ...\n       ...\n       ....\n     ...")
        input("     " + username + " welcome back at first I was scared you weren't going to make it")
        input("     We got there just in time and thanks to your help we were able to take down the Giggle Gang, I'm pround of you")
        quit()
    if score == 15:
        print("Amy Schumer:")
        input("     NO HOW DID YOU DO THIS, ITS IMPOSSIBLE")
        input("*Theres a lound band and you turn around to see*")
        print("Captain Sanjay Patel:")
        input("     It's good to see you, you worked really hard and did an amazing job congratulations the state with definally regognize this, now go get some rest")
        os.system("cls")
        input("*Six Months Later*")
        print("Captain Patel:")
        input("     It is truley my honor to bestowe this medal for their services to this towns hero " + username + " their hardwork took down one of this citys worst crime organizations, for that we thank you")
        quit()
    game("Nick")
