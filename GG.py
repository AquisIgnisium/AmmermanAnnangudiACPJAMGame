import os
import challenge
def game(username):
    print("Chief Patel:")
    input("     Good choice, I mean you should be able to do this without much struggle, I was hoping you would've picked a hard one")
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
        input("     The Giggle Gang is a surprisingly serious group of criminals. They kidnap children and take away their happyness or ""giggles"". The group is led by Amy Schumer, the worst comedian in my opinion, but that doesn't matter right now. I need you to go infiltrate them and take Schumer down. Good luck I hope to see you back soon.")
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
    print("Choose a responce Responce 1:""I wont let you down.""\nRespoce 2:""Already!?""\nResponce 3:Stay silent")
    speaking_choice2 = input(">>")
    if speaking_choice2 == "1":
        print(undercover_username + ":")
        input("     I wont let you down.")
    elif speaking_choice2 == "2":
        print(undercover_username + ":")
        input("     Already!?")
    elif speaking_choice2 == "3":
        print("\n\n")
    input("Complete this mini game to carry out your task")
    challenge_1 = challenge.dnaBases(2,20)
