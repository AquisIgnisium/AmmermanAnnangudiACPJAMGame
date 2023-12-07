import challenge
import os as os
import time as time
import random as rand
from random import shuffle
import string

def game(username):
    os.system('cls')
    print("Chief Patel:")
    input("     Interesting choice" + username)
    input("     I think that if you put your head down and attack this gang with all of your gang, you can win")
    input("     Before I send you off, what is your undercover name?")
    undercoverName = input(">>")
    os.system('cls')
    print("Julian Denburg (Black Diamond Grunt)")
    input("     Get up!")
    input("*You wake up to Julian holding a gun against your temple. His haircut is choppy and uneven*")
    input("Disarm the Gun!")
    challenge.closebrackets(1,10)
game("Charan")