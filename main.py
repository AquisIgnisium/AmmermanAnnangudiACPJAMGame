import BDS
import GG
import SOS

def Game():
    print("Welcome to...")
    print("""
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\    _________  ___  ___  _______                                                / /\ 
/ /\ \  |\___   ___\\  \|\  \|\  ___ \                                              / /\ \
\ \/ /  \|___ \  \_\ \  \\\  \ \   __/|                                             \ \/ /
 \/ /        \ \  \ \ \   __  \ \  \_|/__                                            \/ / 
 / /\         \ \  \ \ \  \ \  \ \  \_|\ \                                           / /\ 
/ /\ \         \ \__\ \ \__\ \__\ \_______\                                         / /\ \
\ \/ /          \|__|  \|__|\|__|\|_______|                                         \ \/ /
 \/ /                                                                                \/ / 
 / /\                                                                                / /\ 
/ /\ \                                                                              / /\ \
\ \/ /   ________  ___       _______   _______   ________  _______   ________       \ \/ /
 \/ /   |\   ____\|\  \     |\  ___ \ |\  ___ \ |\   __  \|\  ___ \ |\   __  \       \/ / 
 / /\   \ \  \___|\ \  \    \ \   __/|\ \   __/|\ \  \|\  \ \   __/|\ \  \|\  \      / /\ 
/ /\ \   \ \_____  \ \  \    \ \  \_|/_\ \  \_|/_\ \   ____\ \  \_|/_\ \   _  _\    / /\ \
\ \/ /    \|____|\  \ \  \____\ \  \_|\ \ \  \_|\ \ \  \___|\ \  \_|\ \ \  \\  \|   \ \/ /
 \/ /       ____\_\  \ \_______\ \_______\ \_______\ \__\    \ \_______\ \__\\ _\    \/ / 
 / /\      |\_________\|_______|\|_______|\|_______|\|__|     \|_______|\|__|\|__|   / /\ 
/ /\ \     \|_________|                                                             / /\ \
\ \/ /                                                                              \ \/ /
 \/ /                                                                                \/ / 
 / /\    ________  ________  _______   ________   _________                          / /\ 
/ /\ \  |\   __  \|\   ____\|\  ___ \ |\   ___  \|\___   ___\                       / /\ \
\ \/ /  \ \  \|\  \ \  \___|\ \   __/|\ \  \\ \  \|___ \  \_|                       \ \/ /
 \/ /    \ \   __  \ \  \  __\ \  \_|/_\ \  \\ \  \   \ \  \                         \/ / 
 / /\     \ \  \ \  \ \  \|\  \ \  \_|\ \ \  \\ \  \   \ \  \                        / /\ 
/ /\ \     \ \__\ \__\ \_______\ \_______\ \__\\ \__\   \ \__\                      / /\ \
\ \/ /      \|__|\|__|\|_______|\|_______|\|__| \|__|    \|__|                      \ \/ /
 \/ /                                                                                \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
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
    input("    and the final one is the notorious Giggle Gange, written about for their humourous practices")
    input("    So, tell me your choice by telling me the exact name with capitals of the Gang you wish to challenge")
    choice = input(">>")
    if choice == "Giggle Gang" or choice == "The Giggle Gang":
        GG.game(username)
    elif choice == "Syndicate of Silence" or choice == "The Syndicate of Silence":
        SOS.game(username)
    elif choice == "Black Diamond Syndicate" or choice == "The Black Diamond Syndicate":
        BDS.game(username)

Game()