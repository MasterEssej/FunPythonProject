
import os
import FunnyFunctions as ff

GameActive = True
while(GameActive):
    print("""
---------------------
Welcome to Funny Game!
---------------------
""")
    
    Playing = False
    
    choice = input("Type 'Play' to play the game or 'Quit' to quit: ")
    while (choice.lower() != 'play' and choice.lower() != 'quit'):
        ff.CheckImage(choice)
        choice = input("Type 'Play' to play the game or 'Quit' to quit: ")
    if(choice.lower() == 'quit'):
        GameActive = False
        break
    if(choice.lower() == 'play'):
        Playing = True
        
    while(Playing):
        print("""
---------------------
You are standing at a crossroads.
Do you go to the Forest or the Town?
---------------------
""")
        
        choice = input("Type 'Forest' to go to the forest or 'Town' to go to the town: ")
        while (choice.lower() != 'forest' and choice.lower() != 'town'):
            if(choice.lower() == 'quit'):
                Playing = False
                break
            choice = input("Type 'Forest' to go to the forest or 'Town' to go to the town: ")
        if(choice.lower() == 'forest'):
            exec (open("Forest.py").read())
        elif(choice.lower() == 'town'):
            exec (open("Town.py").read())


