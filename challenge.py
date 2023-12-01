import os as os
import time as time
import random as rand
from random import shuffle
import string
def shuffleWords(w):
    w = list(w)
    shuffle(w)
    return str("".join(w))
def retype(diff, timeReq):
    currTimer = time.time()
    x = ""
    f = diff *5
    for i in range(1,f):
        x = x + rand.choice(string.ascii_letters)
    print("Quick! retype the following characters!")
    print(x)
    userInput = input(">>")
    if userInput == x and time.time()-currTimer < timeReq:
        print("Success!")
        return 1
    else:
        print("Fail!")
        return -1
def dnaBases(diff,timeReq):
    currTimer = time.time()
    bases = ["t","a","c","g"]
    x = ""
    xAnwser = ""
    f = diff *5
    for i in range(1,f):
        x = x + rand.choice(bases)
    for i in x:
        if i == "t":
            xAnwser = xAnwser + "a"
        elif i ==  "a":
            xAnwser = xAnwser + "t"
        elif i == "g":
            xAnwser = xAnwser + "c"
        elif i == "c":
            xAnwser = xAnwser + "g"
    print("Quick! Write the complements to the following bases!")
    print(x)
    userBases = input(">>")
    if userBases == xAnwser and time.time()-currTimer < timeReq:
        print("Success!")
        return 1
    else:
        print("Fail!")
        return -1
def closebrackets(diff,timeReq):
    currTimer = time.time()
    x = ["{","[","(","<"]
    userX = ""
    f = diff *5
    for i in range(1,f):
        userX = userX + rand.choice(x)
    xAnwser = userX + completeBrackets(userX)[::-1]
    print("Quick! Retype it with the matching bracket!")
    print(userX)
    print(xAnwser)
    userInput = input("Anwser:  ")
    if userInput == xAnwser and time.time()-currTimer < timeReq:
        print("Success!")
        return 1
    else:
        print("Fail!")
        return -1
def completeBrackets(b):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}', '<' : ">"}

    for bracket in b:
        if bracket in pairs.keys():
            stack.append(pairs[bracket])
    return ''.join(stack)
def MemoryGame(diff,TimeReq):
    currTimer = time.time()
    x = ""
    f = diff *5
    for i in range(1,f):
        x = x + rand.choice(string.ascii_letters)
    print("Quick! Memorize the string of characters")
    print(x)
    time.sleep(TimeReq)
    os.system('cls')
    input("Press Enter to Continue")
    os.system('cls')
    print("Print out the characters now!")
    userInput = input(">>")
    if userInput == x:
        print("Success!")
        return 1
    else:
        print("Fail!")
        return -1
def wordScramble(diff, timeReq):
    currTimer = time.time()
    common_words = [
    "apple", "table", "chair", "house", "happy",
    "smile", "water", "dance", "write", "learn",
    "light", "music", "sunny", "cloud", "dream",
    "night", "flower", "peace", "green", "heart",
    "laugh", "beach", "money", "brown", "candle",
    "simple", "friend", "family", "yellow", "orange",
    "purple", "forest", "travel", "people", "silent",
    "shadow", "mirror", "window", "silver", "coffee",
    "summer", "winter", "spring", "autumn", "garden",
    "diamond", "butterfly", "freedom", "jungle", "ocean",
    "mountain", "rainbow", "country", "moment", "spirit",
    "captain", "puzzle", "tunnel", "courage", "fortune",
    "whisper", "sunset", "sunrise", "twinkle", "majestic",
    "mystery", "radiant", "fantasy", "curious", "inspire",
    "elegant", "treasure", "genuine", "brilliant", "cascade",
    "velvet", "quiver", "cocoa", "fumble", "climax",
    "rumble", "noodle", "nectar", "glisten", "dazzle",
    "breeze", "serene", "tranquil", "lagoon", "delight",
    "serendipity", "lullaby", "enchant", "whimsical", "velvet",
    "frolic", "sculpt", "harmony", "blossom", "enlighten"]
    userWord = rand.choice(common_words)
    scrambledWord = shuffleWords(userWord)
    print("Quick! Unscramble the word!")
    print(scrambledWord)
    userInput = input(">>")
    if userInput == userWord and time.time()-currTimer < timeReq:
        print("Success!")
        return 1
    else:
        print("Fail!")
        return -1
def arithmatic(diff,timeReq,operator):
    currTimer = time.time()
    num1 = rand.randint(5,diff*5)
    num2 = rand.randint(5,diff*5)
    anwser = 0  
    print("Quick! evaluate the following arithmatic!")
    print(num1, operator, num2)
    if operator == "+":
        anwser = num1 + num2
        x = int(input(">>"))
        if x == anwser and time.time()-currTimer < timeReq:
            print("Success")
            return 1
        else:
            print("Failure!")
            return -1
    if operator == "-":
        anwser = num1 - num2
        x = int(input(">>"))
        if x == anwser and time.time()-currTimer < timeReq:
            print("Success")
            return 1
        else:
            print("Failure!")
            return -1
    if operator == "*":
        anwser = num1 * num2
        x = int(input(">>"))
        if x == anwser and time.time()-currTimer < timeReq:
            print("Success")
            return 1
        else:
            print("Failure!")
            return -1
