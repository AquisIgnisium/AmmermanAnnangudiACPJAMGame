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
    #Maybe some input here?
    input("    Get in Wuss!")
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

