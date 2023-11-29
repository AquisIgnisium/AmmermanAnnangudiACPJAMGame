import os
import challenges
def game(username):
    print("Chief Patel")
    input("     Good choice, I mean you should be able to do this without much struggle, I was hoping you would've picked a hard one")
    print("\n")
    print("how would you like to respond \nResponce 1:""Yea lets just get this over with already.""\nResponce 2:""Lets sart out small what more can you tell me about the Giggle Gang""\nResponce 3:Well the other two sounded a little too dangerous and I want to have some fun")
    speaking_choice1 = input(">>")
    if speaking_choice1 == "1":
        print(username)
        input("     Yea lets just get this over with already.")
        print("Chief Patel")
        input("     Better going then")
    elif speaking_choice1 == "2":
        print(username)
        input("     Lets sart out small what more can you tell me about the Giggle Gang.")
        print("Chief Patel")
        input("     The Giggle Gang is a surprisingly serious group of criminals. They kidnap children and take away their happyness or ""giggles"". The group is led by Amy Schumer, the worst comedian in my opinion, but that doesn't matter right now. I need you to go infiltrate them and take Schumer down. Good luck I hope to see you back soon.")
    elif  speaking_choice1 == "3":
        print(username)
        input("     Well the other two sounded a little too dangerous and I want to have some fun.")
        print("Chief Patel")
        input("     Thats understandable but be warned their crimes are not for the light hearted and their leader is incredibly annoying.")
    print("One last thing before you leave, whats your undercovername")
    undercover_username = input(">>")
    os.system('cls')
    input("The Next Day \n\nYou wake up and put on your new clothes, your no longer " + username + " and you are now " + undercover_username)
    input("For your first day with the giggle gang they task you with kidnaping a few children as a test of loyalty, they know most people can't bring themselves to take a child.")
    input("Complete this mini game to carry out your task")
    challenges.dnaBases(1,15)
game("brr")
