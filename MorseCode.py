import winsound
import string
import time



print("This is an English to Morse converter")
Wordinput = input("Please enter your word:")
Morselength = len(Wordinput)
WordHelp = 0

def MorseAlphabet(n):
    if n.lower() == "a":
        return ". -"
    elif n.lower() == "b":
        return "-..."
    elif n.lower() == 'c':
        return "-.-."    
    elif n.lower() == 'd':
        return "-.."    
    elif n.lower() == 'e':
        return "."
    elif n.lower() == "f":
        return "-..-."
    elif n.lower() == "g":
        return "--."
    elif n.lower() == 'h':
        return "...."
    elif n.lower() == 'i':
        return ".."    
    elif n.lower() == 'j':
        return ".---"    
    elif n.lower() == 'k':
        return "-.-"
    elif n.lower() == 'l':
        return ".-.."
    elif n.lower() == "m":
        return "--"
    elif n.lower() == 'n':
        return "-."
    elif n.lower() == 'o':
        return "---"    
    elif n.lower() == 'p':
        return ".--."    
    elif n.lower() == 'q':
        return "--.-"
    elif n.lower() == 'r':
        return "-.-."
    elif n.lower() == "s":
        return "..."
    elif n.lower() == 't':
        return "-"
    elif n.lower() == 'u':
        return "..-"    
    elif n.lower() == 'v':
        return "...-"    
    elif n.lower() == 'w':
        return ".--"
    elif n.lower() == 'x':
        return "-..-"
    elif n.lower() == 'y':
        return "-.--"    
    elif n.lower() == 'z':
        return "--.."
    elif n == '1':
        return ".---"
    elif n == "2":
        return "..---"
    elif n == '3':
        return "...--"
    elif n == '4':
        return "....-"
    elif n == "5":
        return "....."
    elif n == '6':
        return "-...."
    elif n == '7':
        return "--..."
    elif n == "8":
        return "---.."
    elif n == '9':
        return "----."
    elif n == "0":
        return "-----"
    elif n == ".":
        return ".-.-.-"
    elif n == ",":
        return "--..--"
    elif n == "?":
        return "..--.."
    elif n == "'":
        return ".----."
    elif n == "!":
        return "-.-.--"
    elif n == "/":
        return "-..-."
    elif n == ":":
        return "---..."
    elif n == ";":
        return "-.-.-."
    elif n == "=":
        return "-...-"
    elif n == "+":
        return ".-.-."
    elif n == "-":
        return "-....-"
    elif n == "_":
        return "..--.-"
    elif n == '"':
        return ".-..-"
    elif n == "@":
        return ".--.-."
    elif n == " ":
        return " "
    else:
        return ""








for x in Wordinput:
    for m in MorseAlphabet(x):
        if m == "-":
            winsound.Beep(750, 600)
        if m == ".":
            winsound.Beep(750, 200)
    print(MorseAlphabet(x), end=" ")









    
     

