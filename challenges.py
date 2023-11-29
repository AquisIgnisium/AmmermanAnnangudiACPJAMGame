import os as os
import time as time
import random as rand
import string
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
    userInput = input("Anwser:  ")
    if userInput == xAnwser and time.time()-currTimer < timeReq:
        print("Success!")
        return 1
    else:
        print("Fail!")
        print(xAnwser)
        return -1
def completeBrackets(b):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}', '<' : ">"}

    for bracket in b:
        if bracket in pairs.keys():
            stack.append(pairs[bracket])
    return ''.join(stack)
def arithmatic(diff,timeReq,operator):
    currTimer = time.time()
    num1 = rand.randint(5,diff*5)
    num2 = rand.randint(5,diff*5)
    anwser = 0  
    print("Quick! evaluate the following arithmatic!")
    if operator == "+":
        anwser = num1 + num2
        x = input(">>")
    if operator == "-":
        anwser = num1 - num2
        x = input(">>")
    if operator == "*":
        anwser = num1 * num2
        x = input(">>")
    if operator == "/":
        anwser = num1 / num2
        x = input(">>")
    
retype(1)    
dnaBases(1)
closebrackets(1)