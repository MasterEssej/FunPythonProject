

InForest = True
while(InForest):
    print("""
---------------------
You are in a forest.
---------------------
""")
    
    
    choice = input("Type 'Stay' to stay in the forest or 'Back' to go back to the crossroads: ")
    while (choice.lower() != 'stay' and choice.lower() != 'back'):
        choice = input("Type 'Stay' to stay in the forest or 'Back' to go back to the crossroads: ")
    if(choice.lower() == 'back'):
        InForest = False
        break
    