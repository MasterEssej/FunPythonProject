import ImageStuff as img


# Takes in 2 strings and prints out wether or not the second string is in the first string
def findWordInString(userInput, targetWord):
    inputArray = userInput.split()
    wordFound = False
    for word in inputArray:
        if(word == targetWord):
            print("funny word found :)")
            wordFound = True
            break
    if(wordFound == False):
        print("funny word not found :(")
        
def PrintImage(imagePath):
    img.ImageToASCII(imagePath)
    
def CheckImage(string):
    if(string.lower() == 'yuh'):
        PrintImage(r"c:\Users\jesse.viitanen\Repos\FunPythonProject\FunPythonProject\yuh.jpg")
    if(string.lower() == 'yep'):
        PrintImage(r"c:\Users\jesse.viitanen\Repos\FunPythonProject\FunPythonProject\yep.png")
    if(string.lower() == 'map'):
        PrintImage(r"c:\Users\jesse.viitanen\Repos\FunPythonProject\FunPythonProject\testMap.png")