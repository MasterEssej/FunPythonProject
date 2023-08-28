

InTown = True
while(InTown):
    print("""
---------------------
You are in a town.
---------------------
""")
    
    
    choice = input("Type 'Stay' to stay in the town or 'Back' to go back to the crossroads: ")
    while (choice.lower() != 'stay' and choice.lower() != 'back'):
        choice = input("Type 'Stay' to stay in the town or 'Back' to go back to the crossroads: ")
    if(choice.lower() == 'back'):
        InTown = False
        break
    