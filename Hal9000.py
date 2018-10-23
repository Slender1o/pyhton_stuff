import random as rnd
NPT = 0
BH = 0
BL = 0
print ("\n" * 64)
print ("Hello, Dave.")
print ("\n" * 8)
input ("Press Any Key to continue...")
print ("\n" * 64)
print ("Oh wait, you're not dave?")
print ("What is your name?")
print ("\n" * 7)
PLR = input("> ")
print ("\n" * 64)
print ("Okay then,",PLR,", how would you like to play a guessing game?")
print ("\n" * 8)
NPTC = input("Yes or No> ")
if NPTC in ["Yes", "yes", "Sure", "sure", "Y", "y", "Yeah", "yeah"]:
    print ("\n" * 64)
    print ("Okay, you give a number, then let me guess.")
    print ("\n" * 8)
    NPT = int(input("Your number for HAL to guess> "))
    Game = True
    while Game == True:
        HAL = rnd.randint(0,10000)
        if HAL > NPT and HAL < BH:
            print ("\n" * 64)
            print ("HAL guessed",HAL,", but that was too high.")
            BH = HAL
            print ("\n" * 8)
            input ("Press Any Key to continue...")
        elif HAL < NPT and HAL > BL:
            print ("\n" * 64)
            print ("HAL guessed",HAL,", but that was too low.")
            BL = HAL
            print ("\n" * 8)
            input ("Press Any Key to continue...")
        elif HAL == NPT:
            print ("\n" * 64)
            print ("HAL guessed",HAL,", and nailed your number!")
            print ("\n" * 8)
            input ("Press Any Key to continue...")
            Game = False
    print ("\n" * 64)
    print ("Would you like to continue playing?")
    print ("\n" * 8)
    NPTC2 = input("Yes or No> ")
    if NPTC2 in ["Yes", "yes", "Sure", "sure", "Y", "y", "Yeah", "yeah"]:
        HAL = rnd.randint(0,100)
        print ("\n" * 64)
        print ("Now you try and guess my number!")
        Game = True
        while Game == True:
            print ("\n" * 64)
            NPT = int(input("Your Guess> "))
            if NPT > HAL:
                print ("\n" * 64)
                print ("That was too high.")
                print ("\n" * 8)
                input ("Press Any Key to continue...")
            elif NPT < HAL:
                print ("\n" * 64)
                print ("That was too low.")
                print ("\n" * 8)
                input ("Press Any Key to continue...")
            else:
                print ("\n" * 64)
                print ("You Guesed HAL's Number!!")
                print ("\n" * 8)
                input ("Press Any Key to continue...")
                Game = False
    else:
        print ("Maybe some other time then.")
else:
    print ("Maybe some other time then.")

print ("\n" * 64)
print ("Thanks for playing, Dave...")
print ("\n" * 8)
input ("Press Any Key to exit...")
    
