import BDS
import GG
import SOS
import pygame
from pygame.locals import *
from pygame import mixer

mixer.init()
mixer.music.load('Take Five.wav')
mixer.music.play()


def Game():
    print("Welcome to...")
    print("""
 .--------------------------------------------------------------------------.
| ______   __  __     ______                                               |
|/\__  _\ /\ \_\ \   /\  ___\                                              |
|\/_/\ \/ \ \  __ \  \ \  __\                                              |
|   \ \_\  \ \_\ \_\  \ \_____\                                            |
|    \/_/   \/_/\/_/   \/_____/                                            |
|                                                                          |
| ______     __         ______     ______     ______   ______     ______   |
|/\  ___\   /\ \       /\  ___\   /\  ___\   /\  == \ /\  ___\   /\  == \  |
|\ \___  \  \ \ \____  \ \  __\   \ \  __\   \ \  _-/ \ \  __\   \ \  __<  |
| \/\_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\|
|  \/_____/   \/_____/   \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/|
|                                                                          |
| ______     ______     ______     __   __     ______                      |
|/\  __ \   /\  ___\   /\  ___\   /\ "-.\ \   /\__  _\                     |
|\ \  __ \  \ \ \__ \  \ \  __\   \ \ \-.  \  \/_/\ \/                     |
| \ \_\ \_\  \ \_____\  \ \_____\  \ \_\\"\_\    \ \_\                      |
|  \/_/\/_/   \/_____/   \/_____/   \/_/ \/_/     \/_/                     |
'--------------------------------------------------------------------------'
""")
    input("Press enter to start...")
    print("Please enter your username")
    username = input(">>")
    print("Chief Officer Sanjay Patel:")
    input("    Hey there " + username + "!")
    input("    It's been a while since your last mission...")
    input("    So, I've got a mission for you!")
    input("    I found three notorious underground crime rings in Hebron, Indiana")
    input("    The first one is the powerful Black Diamond Syndicate, famed for their ruthless behavior")
    input("    The second one is the dangerous Syndicate of Silence, known for their strict operations")
    input("    and the final one is the notorious Giggle Gang, written about for their humourous practices")
    input("    So, tell me your choice by telling me the exact name with capitals of the Gang you wish to challenge")
    choice = input(">>")
    if choice == "Giggle Gang" or choice == "The Giggle Gang":
        GG.game(username)
    elif choice == "Syndicate of Silence" or choice == "The Syndicate of Silence":
        SOS.game(username)
    elif choice == "Black Diamond Syndicate" or choice == "The Black Diamond Syndicate":
        BDS.game(username)

Game()
