import re #Library for regular expressions

def isValidCard(userInput): #Checks if the card that is being inputted is valid, like S9 is okay but Z87 is not.
    cardPattern = r"^[HSDC](10|[2-9]|[JQKA])$" #HSDC is the suit and 2-9, 10 and JQKA is the rank, explained more in the reflection

    if re.match(cardPattern, userInput.upper()): #Matches the card pattern to the user's card input, also makes it upper so eg: s5 becomes S5 so it can be validated. 
        return True
    else:
        return False