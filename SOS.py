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
    input("    Ciao, " + undercoverName + "!")
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
    input("A new day...")
    print("Tony Rossi:")
    input("    Wake up little regazzo")
    input("    I have someone new for you to meet!")
    input("    This is Vinny Ferari, the scariest of our grunts!")
    print("Vinny Ferrari (Very Scary):")
    input("    Get ready to go!")
    input("*Vinny chucks a rubiks cube at you*")
    print("Vinny Ferrari:")
    input("    Solve this newbie!")
    challenge2 = challenge.arithmatic(13,15,"*")
    if challenge2 == -1:
        print("Vinny Ferrari:")
        input("    He isn't the cream of the crop, but I could work with this")
    else:
        print("Vinny Ferrari:")
        input("    Excellent regazzo, we've got work today!")
    print("Vinny Ferrari:")
    input("    I am ordering you to commit the biggest crime yet!")
    input("    You will commit an armed robbery tonight against the bank!")
    input("    I order you to rest up until tonight")
    input("*Vinny punches you in the face*")
    print("Vinny Ferrari:")
    input("    Goodnight little man!")
    input("You pass out...")
    os.system('cls')
    input("*You wake up confused back in Tony's van*")
    input("*Two marinara stained masked men throw you out of the car*")
    print("Masked Men:")
    input("     Sayonara Sucka!")
    input("*You see the bank and start working on the lock*")
    winCount = 0
    loseCount = 0
    bank1 = challenge.wordScramble(1,15)
    input("*You mutter as you see a digital PIN pad*")
    if bank1 == -1:
        loseCount += 1
        winCount += -1
        print("*You silently curse as you use the butt of your gun to break the glass, you feel everyone in the vinicinty hear it*")
    else:
        winCount += 1
        print("*You sigh with relief as the door clicks open*")
    bank2 = challenge.dnaBases(3,30)
    if bank2 == -1:
        loseCount += 1
        winCount += -1
    else:
        winCount += 1
    input("*As you push through the door you have to enter the PIN again!*")
    bank3 = challenge.MemoryGame(3,15)
    if bank3 == -1:
        loseCount += 1
        winCount += -1
        print("*Your face burns as you smack the butt of your gun against the glass*")
    else:
        winCount += 1
        print("*The PinPad turns green and lets out an alarming beep*")
    input("*You see a security guard peek out at you across the room! You have to shoot him*")
    man1 = challenge.arithmatic(2,5,"-")
    if man1 == -1:
        loseCount += 1
        winCount += -1
        print("*Your shot soars through the air and shatters some glass, the guard runs away to phone the police*")
    else:
        winCount += 1
        print("*The shot rings out as the guard slumps over clutching his arm!*")
    input("*Another guard comes out of the restroom with guns blazing!*")
    man2 = challenge.arithmatic(2,7,"+")
    if man2 == -1:
        loseCount += 1
        winCount += -1
        print("*You scream as the shot pinches through your arm, the guard runs away to press the silent alarm*")
    else:
        winCount += 1
    input("*Grabbing a magazine out of your pocket, you reload your firearm!*")
    reload1 = challenge.retype(2,10)
    if reload1 == -1:
        loseCount += 1
        winCount += -1
        print("*The magazine misses the slot and slides up smashing into your index finger*")
        print("*Your finger scorches with pain, but you know you must continue*")
    else:
        winCount += 1
        print("The satisfying click of the gun eminates, your raise your firearm again!")
    input("*The janitor comes out of the closet with a phone in his hand. The phrase no witnesses rings across your head*")
    man3 = challenge.arithmatic(3,6,"*")
    if man3 == -1:
        loseCount += 1
        winCount += -1
        print("You can't bring your self to kill the janitor! You tell him to run away")
    else:
        winCount += 1
        print("The bullet impacts the janitor with a thud, his body falls to the ground")
    if loseCount > 5:
        print("Cop sirens ring out as your here the SWAT team break into the building")
        print("    Sanjay Patel:")
        input("    Explain" + username)
        input("    What is the meaning of this?")
        print("How would you like to respond \nResponce 1:""It was for the cover""\nResponce 2:""I'm done with the police, the gang is much more welcoming""\nResponce 3: I don't know (sobbing into hands)")
        speaking_choice1 = input(">>")
        if speaking_choice1 == "1":
            print(username + ":")
            input("     It was for the cover.")
            print("Chief Patel:")
            input("     This wasn't needed for the cover")
            input("     These deaths were meaningless and wasted")
            input("     I am disapointed in the lack of ethics you displayed")
            input("     Because of this, you will be prison for a long time")
            print("*The officers drag you to their car*")
            print("*You scream and kick knowing that your life is over*")
            quit()
        elif speaking_choice1 == "2":
            print(username + ":")
            input("     I'm done with the police, the gang is much more welcoming")
            print("Chief Patel:")
            input("    Then you know where you are going right!")
            input("    I hate gang members, but do you know who I hate more?")
            input("    Betrayers")
            quit()
        else:
            print(username + ":")
            input("     I don't know (sobbing into hands)")
            print("Chief Patel:")
            input("     I don't care if you don't know ")
            input("     You ruined YOUR life, so prison if the next event!")
            quit()
    else:
        input("*A white van flys down the corner to the bank*")
        print("The Jester:")
        input("     GET IN YOU UN GARLICED KNOT")
        input("     CAN'T HEAR YOU LISTENING TO PIZZA MUSIC")
        input("     JUST SLEEP ILL TAKE YOU BACK")
        print("*You fall asleep to a whispering sound of pizza music*")
    os.system('cls')
    print("*You wake up to The Jester slapping your face*")
    print("The Jester:")
    input("     heya kid, my name is Joey Volpe")
    input("     I shouldn't be tellin ya this but")
    input("     I also work for the cops, ill hook ya up with the gang boss, Jimmy Santoro")
    input("     getcha fingas ready and fight!")
    os.system("cls")
    print("Jimmy \"The Joker \"Santoro:")
    input("     Welcome to da family I've heard so a much abouta ya")
    input("     What ya did at that back robbery was real impressive")
    input("     I want ya to come work with me, be one of da big dawgs")
    input("     But first i need ya to do somthing for me")
    input("     Joey here is a cop and I want ya to take em down")
    input("     What'dya ya say")
    print("\n \nYou have two responce choices\nResponce 1:\"Of course boss anything you say\"\nResponce 2:\"Hell no Joey lets get this guy\"")
    speaking_choice2 = input(">>")
    if speaking_choice2 == "1":
        print("Joey Volpe:")
        input("     What da hell bro, bring it them")
        joey_responses = ["I can't believe you would do this to me after everything we've been through." , "I thought I could trust you, but I guess I was wrong." , "You're not the person I thought you were." , "I never expected you to betray our friendship like this." , "I feel hurt and betrayed by your actions." , "How could you be so selfish and disregard our friendship?" , "I never thought our friendship would end like this." , "I need some time and space to process what you've done." , "I hope one day you realize the impact of your betrayal." , "I deserve better than a friend who would betray me." , "How could you do this to someone who cared about you?" , "I'm disappointed in you and the choices you've made." , "You've shattered my faith in our friendship." , "I never saw this coming from someone I considered a friend." , "I deserve friends who won't betray me."]
        lose_count = 0
        score = 0
        while lose_count < 3 and score < 15:
            challenge_11 = challenge.arithmatic(2,20,"*")
            if challenge_11 == 1:
                score += 1
            elif challenge_11 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Joey Volpe:")
            input("     " + rand.choice(joey_responses))
            challenge_12 = challenge.wordScramble(1,20)
            if challenge_12 == 1:
                score += 1
            elif challenge_12 == -1:
                    lose_count = lose_count + 1
            if lose_count == 3 or score == 15:
                break
            print("Joey Volpe:")
            input("     " + rand.choice(joey_responses))
            challenge_13 = challenge.dnaBases(3,15)
            if challenge_13 == 1:
                score += 1
            elif challenge_13 == -1:
                lose_count = lose_count + 1
            if lose_count == 3 or score == 15:
                break
            print("Joey Volpe:")
            input("     " + rand.choice(joey_responses))
            challenge_14 = challenge.closebrackets(2,20)
            if challenge_14 == 1:
                score += 1
            elif challenge_14 == -1:
                lose_count = lose_count + 1
            if lose_count == 3 or score == 15:
                break
            print("Joey Volpe:")
            input("     " + rand.choice(joey_responses))
            challenge_15 = challenge.MemoryGame(1,10)
            if challenge_15 == 1:
                score += 1
            elif challenge_15 == -1:
                lose_count = lose_count + 1
            if lose_count == 3 or score == 15:
                break
            print("Joey Volpe:")
            input("     " + rand.choice(joey_responses))
            challenge_16 = challenge.retype(3,15)
            if challenge_16 == 1:
                score += 1
            elif challenge_16 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Joey Volpe:")
            input("     " + rand.choice(joey_responses))
        if lose_count == 3:
            print("Joey Volpe:")
            input("     I cant belive that you betrayed me, justa like that")
            input("     Good bye " + undercoverName)
            quit()
        elif score == 15:
            print("Joey Volpe:")
            input("     Why'd you do it, I thoght you and I were the same")
            print("Jimmy Santoro:")
            input("     I'm proud of ya kid, good job taking him down")
            input("     Lets go tell everyone who the new jester is")
            quit()
    elif speaking_choice2 == "2":
        print("Joey Volpe:")
        input("     Sorry kid your on your own")
        print("\"The Joker\"")
        input("     Ha your only friend left you, take this")
        Joker_responses = ["Where do you think you're goin'? You can't escape!" , "I will make you pay for what you've done!" , "I'm tired of your lies and your manipulations!" , "Don't treat me like this, have some respect for yourself!" , "You're outta your mind! I can't believe the nonsense you're sayin'!" , "Don't push me against the wall, you might regret it!" , "Your arrogance will get you nowhere!" , "Don't you dare speak to me like that!" , "You're just a coward. You can't face the truth!" , "Enough! I can't take these senseless arguments anymore!" , "Ay, you think you can mess with me?! I show you what I'm made of!" , "Come on, come on! Let's settle this like a real man, eh?" , "You better watch your back, my friend. You haven't seen the last of me!" , "I will make you regret the day you crossed paths with me, capisce?" , "You think I'm afraid? You got another thing comin', mio amico!" , "I don't need your pity. I'll fight tooth and nail till the end!" , "You're gonna wish you never laid eyes on me, trust me on that!" , "I may be small, but I'm fierce! I'll knock you out in one hit!"]
        lose_count = 0
        score = 0
        while lose_count < 3 and score < 15:
            challenge_11 = challenge.arithmatic(2,20,"*")
            if challenge_11 == 1:
                score += 1
            elif challenge_11 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Jimmy Santoro:")
            input("     " + rand.choice(Joker_responses))
            challenge_12 = challenge.wordScramble(2,20)
            if challenge_12 == 1:
                score += 1
            elif challenge_12 == -1:
                    lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Jimmy Santoro:")
            input("     " + rand.choice(Joker_responses))
            challenge_13 = challenge.dnaBases(3,15)
            if challenge_13 == 1:
                score += 1
            elif challenge_13 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Jimmy Santoro:")
            input("     " + rand.choice(Joker_responses))
            challenge_14 = challenge.closebrackets(2,20)
            if challenge_14 == 1:
                score += 1
            elif challenge_14 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Jimmy Santoro:")
            input("     " + rand.choice(Joker_responses))
            challenge_15 = challenge.MemoryGame(1,1)
            if challenge_15 == 1:
                score += 1
            elif challenge_15 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Jimmy Santoro:")
            input("     " + rand.choice(Joker_responses))
            challenge_16 = challenge.retype(3,15)
            if challenge_16 == 1:
                score += 1
            elif challenge_16 == -1:
                lose_count += 1
            if lose_count == 3 or score == 15:
                break
            print("Jimmy Santoro:")
            input("     " + rand.choice(Joker_responses))
        if lose_count > 3:
            print("Jimmy Santoro:")
            input("     I cant belive ya thought you would win, its kinda funy actually")
            input("     Ya shoulda taken my offer, bye bye")
            quit()
        if score == 15:
            print("Jimmy Santoro:")
            input("     How'd ya manage that one")
            input("     Maybe you're better than a thought")
            print("Joey Volpe:")
            input("     Did I make it in time, I brought basckup")
            input("     Wow i cant believe you took him down, and all by yourself too, thats real impresive, now you go home and get some rest, oh and good job")
            quit()