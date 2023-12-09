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
    print("Chose something to say\nChoice 1:\"Is this how it normally is here?\"\nChoice 2:\"Anything you say\"\nChoice 3:Stay silent")
    speaking1 = input(">>")
    print(undercoverName + ":")
    if speaking1 == "1":
        input("     Is this how it normally is here?")
        print("Julian Denburg:")
        input("     Shut up, ypu worthless piece of...")
    elif speaking1 == "2":
        input("     Anything you say")
        print("Julian Denburg:")
        input("     Shut up, ypu worthless piece of...")
    elif speaking1 == "3":
        input("     ...\n       ...\n       ...")
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
    input("*Julian drags you away*")
    print("Julian Denburg:")
    input("    How did you do that??")
    input("    The last guy that cooked for Harloff was killed horribly")
    input("    I think you need to meet Andrew, he wil be a larger challenge for you")
    input("*As if it were on cue, a thin bald man walks into the room*")
    print("Andrew Johnson (Black Diamond Grunt)")
    input("    Rise and shine squirt")
    input("    Here comes the real fun, today we break a friend out of jail")
    input("    After you take a nice little nap, we head to Hebron County Jail")
    input("    Once there, we get rid of guards and break our dear friend Franz Ferling out of jail")
    input("    So lets get you started on that nap, shall we?")
    input("*The world blacks out as a wrinkled fist is te last thing you see*")
    os.system('cls')
    print("Andrew Johnson:")
    input("    I think some nice cold water is just what you need")
    input("    Or the last thing you need...")
    input("*Dodge Andrew's bucket of ice!*")
    userChallenge7 = challenge.MemoryGame(2,5)
    if userChallenge7 == -1:
        input("*Andrew pulls a pistol out of his pocket*")
        print("Andrew Johnson:")
        input("    Maybe you aren't cut out for gang life after all")
        input("*Andrew empties the pistol*")
        input("You Lose!")
        quit()
    else:
        input("*You chop the bucket mid air and combat roll away*")
    print("Andrew Johnson:")
    input("    Nice job dodging that rookie!")
    input("    I just hope that you dropped all that moral stuff")
    input("*Andrew leads you out to his van*")
    input("*The ceiling of the back of the van is covered with knives*")
    input("*They are loosely held in place by scotch tape*")
    print("Andrew Johnson:")
    input("    Looks like I forgot about that one.")
    input("    It's not that bad")
    print("Choose something to say\nChoice 1:\"What do you mean it's not that bad I'm gonna die\"\nChoice 2:\"You right fam\"\nChoice 3:\"Whatever you say man\"\n")
    speaking2 = input(">>")
    if speaking2 == "1":
        print(undercoverName + ":")
        input("     What do you mean it's not that bad I'm gonna die")
        print("Andrew Johnson")
        input("    Get in Wuss!")
    elif speaking2 == "2":
        print(undercoverName + ":")
        input("     You right fam")
        print("Andrew Johnson")
        input("    Ok then")
    elif speaking2 == "3":
        print(undercoverName + ":")
        input("     Whatever you say man")
        print("Andrew Johnson")
        input("    Ok then")
    input("*He shoves you in the back of the car*")
    input("*You hear the front door shut and the engine rev on*")
    print("Dodge the Falling knives!")
    knivesDodged = 0
    impalePart = ["head","scapula","eye","fingernail","liver","thyroid","pituatary gland", "glute", "forehead"]
    while knivesDodged<10:
        userChallenge8 = challenge.dnaBases(2,7)
        if userChallenge8 == -1:
            input("*A knife impales you through the",rand.choice(impalePart)+"*")
            input("You Lose!")
            quit()
        else:
            knivesDodged += 1
            print("Only " + str(10-knivesDodged) + " Knives left")
    input("*The van grinds to a halt*")
    input("*The front door opens and then your door opens*")
    print("Andrew Johnson:")
    input("    Man am I suprised you got through that one!")
    input("    The last guy who was in there came out like sushi")
    input("    I think it's time to start the jail break!")
    input("    I mean it's time for you to start the jail break!")
    print_slow("    NOW")
    input("*You start running into the prison, one of the knives in hand*")
    input("*No time for morals now*")
    print("Kill the Guards!")
    GuardCount = 15
    painWords = [
    "    You're hurting me!",
    "    Stop, please! It's too much!",
    "    Why are you doing this to me?",
    "    I beg you, don't hurt me like this!",
    "    No more, I can't take it!",
    "    Please have mercy!",
    "    What have I done to deserve this pain?",
    "    It's like torture!",
    "    Someone help! They're hurting me!",
    "    Get the Knife away from me! Please!",
    "    May Kreke save me! Please save me!",
    "    Tell them I wasn't supposed to be 5th chair! Ahhh!"
]

    while GuardCount > 0:
        if GuardCount != 1:
            print("Only " + str(GuardCount) + " Left!")
        else:
            print_slow("Only one guard left!")
        userChallenge9 = challenge.closebrackets(2,10)
        if userChallenge9 == -1:
            input("*The knife slips out of your hands*")
            input("*Your body was unrecognizable afterwards*")
            if GuardCount == 15:
                print_slow("You did the right thing")
            else:
                print_slow("Your Fault")
            input("You Lose!")
        else:
            print("Guard:")
            input(rand.choice(painWords))
            GuardCount = GuardCount - 1
    input("It's over now")
    input("All you remember was a blur of red")
    print_slow("All Red")
    input("*Andrew grabs your shoulder*")
    print("Andrew Johnson:")
    input("    Now THAT!")
    input("    That was impressive")
    input("    Let me introduce you to someone!")
    print("Kyle Pote:")
    input("    Heya kid!")
    input("    Now are ya rushin or are ya draggin")
    input("    ...")
    input("    Don't anwser that")
    input("*Pote sees your troubled look and takes you back*")
    input("*Your thought blur until the stopping of the car shakes you up*")
    print("Kyle Pote:")
    input("    We're Here")
    print_slow("    now what do you really want?")
    print(username + ":")
    input("    To end Harloff")
    print("Kyle Pote:")
    input("    Then that is what you shall get")
    input("*You turn to look at the door of the house*")
    input("*You turn back and Pote is gone*")
    input("*The stairs of the porch feel harsher than usual*")
    print_slow("Christopher Harloff")
    input("    WHO COMES HERE")
    print(username + ":")
    input("    I")
    input("    I come here")
    print_slow("    TO KILL YOU")
    HarloffDiaologue = [
    "    I'll crush you like a bug!",
    "    Your moves are more out of sync than a kindergarten recital!",
    "    You're about to face the fury of a true powerhouse!",
    "    Is this a fight or a nap? Wake up and face your doom!",
    "    Prepare for annihilation!",
    "    Your rhythm is so off, even the metronome is embarrassed!",
    "    Witness the might of my colossal strength!",
    "    I bet even the tuba players could outrun you!",
    "    Your defeat is inevitable, weakling!",
    "    I've had tougher challenges from my morning warm-up!",
    "    I'll grind your bones to dust!",
    "    You're less coordinated than a one-man band with two left feet!",
    "    You're insignificant in the face of my power!",
    "    I expected a challenge, not a comedy show! Step up your game!",
    "    Bow before your impending demise!",
    "    I've seen better footwork from a three-legged turtle!",
    "    I'll make you regret challenging me!",
    "    Your moves are so slow; even the snare drum is outpacing you!",
    "    Scream for mercy as I unleash my wrath!",
    "    I've seen scarier kittens!"]
    print_slow("HARLOFF APPROACHES")
    harloffAttacks = 30
    while harloffAttacks > 0:
        print("Christopher The Cavon Harloff")
        input(rand.choice(HarloffDiaologue))
        userChallenge10 = challenge.arithmatic(rand.randint(11,14),10,"*")
        if userChallenge10 == -1:
            print("HARLOFF ENDS YOU")
            print_slow("How does it feel now?")
            input("You Lose!")
            quit()
        else:
            harloffAttacks = harloffAttacks - 1
            print("You chop off Harloff's " + rand.choice(impalePart))
            print("Only " + str(harloffAttacks) + " Left!")
        print("Christopher The Cavon Harloff")
        input(rand.choice(HarloffDiaologue))
        userChallenge11 = challenge.closebrackets(4,10)
        if userChallenge11 == -1:
            print("HARLOFF ENDS YOU")
            print_slow("How does it feel now?")
            input("You Lose!")
            quit()
        else:
            harloffAttacks = harloffAttacks - 1
            print("You chop off Harloff's " + rand.choice(impalePart))
            print("Only " + str(harloffAttacks) + " Left!")
        print("Christopher The Cavon Harloff")
        input(rand.choice(HarloffDiaologue))
        userChallenge12 = challenge.dnaBases(5,14)
        if userChallenge12 == -1:
            print("HARLOFF ENDS YOU")
            print_slow("How does it feel now?")
            input("You Lose!")
            quit()
        else:
            harloffAttacks = harloffAttacks - 1
            print("You chop off Harloff's " + rand.choice(impalePart))
            print("Only " + str(harloffAttacks) + " Left!")
        userChallenge13 = challenge.retype(3,10)
        print("Christopher The Cavon Harloff")
        input(rand.choice(HarloffDiaologue))
        if userChallenge13 == -1:
            print("HARLOFF ENDS YOU")
            print_slow("How does it feel now?")
            input("You Lose!")
            quit()
        else:
            harloffAttacks = harloffAttacks - 1
            print("You chop off Harloff's " + rand.choice(impalePart))
            print("Only " + str(harloffAttacks) + " Left!")
        print("Christopher The Cavon Harloff")
        input(rand.choice(HarloffDiaologue))
        userChallenge14 = challenge.wordScramble(5,10)
        if userChallenge14 == -1:
            print("HARLOFF ENDS YOU")
            print_slow("How does it feel now?")
            input("You Lose!")
            quit()
        else:
            harloffAttacks = harloffAttacks - 1
            print("You chop off Harloff's " + rand.choice(impalePart))
            print("Only " + str(harloffAttacks) + " Left!")
    input("*The body of the titanous man falls to the ground with a thud*")
    print_slow("Happy Now?")
    input("*Chief Patel bursts throught the door followed by a SWAT team*")
    input("*Patel and the SWAT Team stare at your goried body and the body of Harloff*")
    input("*They are shocked out of their minds*")
    print("Chief Patel:")
    input("    Do you need some time?")
    print("\n \nYou have two responce choices\nResponce 1:\"I need some time\"\nResponce 2:\"This is my gang now\"")
    speaking_choice4 = input(">>")
    if speaking_choice4 == 1:
        print(username + ":")
        input("     I need some time, GET OUT")
        print_slow("*You stare at the massive titains body on the ground*")
        print_slow("*You question if it was worth it*")
        print_slow("*You grab the concealed knife hidden under the massive rolls of fat and*")
        input("*SNIP*")
        os.system("cls")
        print("Chief Patel:")
        input("Today we morn the loss of a great detective and an amazing person, " + username)
        input("We say our final goodbyes and we wish him happiness in the next life")
        quit()
    elif speaking_choice4 == "2":
        print(username + ":")
        input("     This is my gang now, Ill give you one chance to leave")
        print("Chief Patel:")
        print_slow("     Your better than this you dont have to...")
        input("BANG")
        print_slow("*Chief Patel's lifeless body falls to the ground and a loud thud is heard as the skin of Patel smashes again the massive corpse of Matthew Harloff*")
        os.system("cls")
        input( "*Town under the management of new company led by former cop under the name " + undercoverName + " *")
        quit()