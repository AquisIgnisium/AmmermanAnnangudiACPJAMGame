import BDS
import GG
import SOS


def Game():
    print("Welcome to...")
    x = """
 ______   __  __     ______        ______     __         ______     ______     ______   ______     ______        ______     ______     ______     __   __     ______  
/\__  _\ /\ \_\ \   /\  ___\      /\  ___\   /\ \       /\  ___\   /\  ___\   /\  == \ /\  ___\   /\  == \      /\  __ \   /\  ___\   /\  ___\   /\ "-.\ \   /\__  _\ 
\/_/\ \/ \ \  __ \  \ \  __\      \ \___  \  \ \ \____  \ \  __\   \ \  __\   \ \  _-/ \ \  __\   \ \  __<      \ \  __ \  \ \ \__ \  \ \  __\   \ \ \-.  \  \/_/\ \/ 
   \ \_\  \ \_\ \_\  \ \_____\     \/\_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\     \ \_\ \_\  \ \_____\  \ \_____\  \ \_\\"\_\    \ \_\ 
    \/_/   \/_/\/_/   \/_____/      \/_____/   \/_____/   \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/      \/_/\/_/   \/_____/   \/_____/   \/_/ \/_/     \/_/ 
    """
    print(x)
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
    choice = input("    So, tell me your choice by telling me the exact name with capitals of the Gang you wish to challenge")
    if choice == "Giggle Gang" or choice == "The Giggle Gang":
        GG.game()
    elif choice == "Syndicate of Silence" or choice == "The Syndicate of Silence"

Game()