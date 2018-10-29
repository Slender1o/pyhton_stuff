'''
    Software Engineer: Martin Belt
    Date: 10/14/18
    Time: 6:47 PM CST
    Program: txt.exe

    Co-Developer: George W. F. Downing
    Joined: 10/25/18
    Time: 9:05 AM CST
'''
import time
import random
import sys

def wait(wait):
    time.sleep(wait)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

def raceI(WTR,CLTHSM,CLTHSF,RCE,INTRO):
    WTR = str(WTR)
    CLTHSM = str(CLTHSM)
    CLTHSF = str(CLTHSF)
    INTRO = str(INTRO)
    delay_print(INTRO+RCE[2]+" .")
    if  gender == 'Female':
        delay_print(" You can't help but feel nauseous while in the "+WTR+" of water.\n")
        response = input("Would you like to get out?\n")
        if response == 'Yes':
            goodResponse = response
            if  goodResponse == 'Yes':
                  print("You get out of the water. "+CLOTHSF)
        if response == 'No':
            badResponse = response
            while(badResponse == 'No'):
                print("You think that you should stay in the water for a little while longer.\n")
                input("Would you like to get out?\n")
    if gender == 'Male':
        delay_print(" You can't help but feel nauseous while in the "+WTR+" of water.\n")
        response = input("Would you like to get out?\n")
        if response == 'Yes':
            goodResponse = response
            if  goodResponse == 'Yes':
                  print("You get out of the water. "+CLOTHSM)
        if response == 'No':
            badResponse = response
            askAgain = input("Would you like to get out?\n")
            if (askAgain == 'Yes'):
                print("yes")
    

print ("\n" * 64)

delay_print ("You are surrounded in darkness. Everything that you see is dark and confusing.\n\n")

wait(6)

delay_print("A warm light surrounds you and you hear a voice:\n\n")

wait(3)

Name = input("Who are you, Adventurer? What is your proper name?\n\n>")

nickName = input("..and your nickname, " + Name + "?\n\n>")

wait(1)

delay_print(name + "...that is a good, strong name. ")

delay_print("You have a choice, " + nickName + ". You can become the fabled hero of Falte or you can die in the process.")

delay_print(" I will now transport you into the country of Falte...\n")

time.sleep(6)

delay_print("You wake up in a pool of soothing water. Your memory is hazy, at best, and you can't seem to figure out where you are.")

delay_print(" As you look around, you can't seem to figure out what your body looks like. You try to remember...\n")

print("-------------------------------------------------------\n")



delay_print("As you inspect what little you can see of your body, you remember that you are...\n")

gender = input("What is your gender?\n")

if (gender == 'Female'):

   delay_print("Right. You remember your feminine charms and whims. You are a woman.\n")

if (gender == 'Male'):

   delay_print("Right. You remember your manly muscles and all your feats of strength. You are a man.\n")

wait(6)

print ("\n" * 64)

raceList = [' ', 'Orc', 'Human', 'Elf', 'Dwarf', '']

for i in range(1, 6):

    print(raceList[i])

    print("\n")
    

    

race = input("What is your race, " + Name + "?\n")

delay_print("Yes. That's right. You're a(n) " + race + ".")

time.sleep(5)

print ("\n" * 64)

if race == 'Elf':

    raceI("pool","There is a tunic and a pair of boots.","There is a dress, a hair clip and a pair of boots.",

          ["Elf","elf","Elven","elven"],"You look around and see that you are in a tent with guards standing outside. They are ")






























