import os as os
import time as time
import random as rand
from random import shuffle
import string
import challenge
import os as os
def game(username):
    
    print("Chief Patel:")
    input("    Excellent Choice, I will look forward to watching you decimate the gang from the inside out!")
    input("    Before I send you off, what would you like your undercover name to be?")
    undercoverName = input(">>")
    print("Tony Rossi (Syndicate of Silence Grunt):")
    input("    Ciao, newbie!")
    input("    Welcome to da Family! As you are a newbie, we require you to do some of da tasks to join da Familie")
    input("    Ya gotta rob dis bank. Ya gotta leave nona da witnesses. YA GOTTA GET DA MONEY")
    input("    Veni Vidi Vici BABY. Mamma Mia!")
    os.system('cls')
    input("*Tony leads you out to his rusty white van*")
    input("*He shakily drives you both at 3:30am to a bank in downtown Clinton, IN*")
    input("*He throws out of the van*")
    print("Tony Rossi:")
    input("    Veni Vidi Vici! Sayonora!")
    input("*You walk up to the door of the building and take a look at the hard metal padlock*")
    input("*You pull a hairpin out and start to try to pick the lock*")
    input("*You have 25 seconds before the cops arrive*")
    entryChallenge = challenge.closebrackets(2,25)
    if entryChallenge == 1:
        input("*You feel a breath behind your neck*")
        input("*It reeks of pizza sauce and beef meat*")
        print("Tony Rossi:")
        input("    You hava some of da Talent I see!")
        input("    I willa remember dis!")
        startingTalent = 1
    else:
        input("*You feel a sandwich pressed against the back of your head*")
        print("Tony Rossi:")
        input("    Mamma Mia have ya gotta lot to learn!")
        input("    Tis a Fine!")
        startingTalent = 0
    input("*Tony grabs you by the shirt and pulls you back to the van, which was hidden*")
    input("*The van was inconspuously hidden behind a comicly large meatball sub*")
    print("Tony Rossi:")
    input("    Ya got spunk kid. Ya got spunk")
    input("    When we get back to da Family House I needcha to get some sleep")
    input("*Tony put's on a pair of pizza glasses and looks through the window*")
    input("*It's 3:50am in the morning and pitch black outside*")
    input("*You arive back at the dark brown mansion*")
    input("*Tony leads you to your room, which you share with mold on a piece of cheese and a rat*")
    print("Tony Rossi:")
    input("    Marinara flavored dreams little regazzo!")
    input("You drift to sleep with the smell of marinara in your nose")
    os.system('cls')
    
game("Charan")