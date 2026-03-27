from cardChecker import isValidCard #Imported so I can check if the inputted card is valid or not
from deck import Deck #Imported so we can use the deck to deal the cards to the players
from players import User, AI #Imported so we can have the players being the user and the AI to play against each other. 

def main():
    deck = Deck() #Creating the deck of cards
    deck.shuffleDeck() #Making the cards random
    
    human = User("Player 1", 100, "Dealer") #This is the user, gives the name, balance and the position from its sub class
    computer = AI("CPU", 100, "Hard") #This is the AI, gives the name, balance and the difficulty from its sub class
    
    human.hand.append(deck.deal()) #Deals one card to the player
    computer.hand.append(deck.deal()) #Deals one card to the AI
    
    print(f"Welcome. Your hand is {human.hand[0]}") #Tells the player what their first card is. 
    
    check = input("Type your card in the format S6 or HK): ") #Asks the player what they want their second card to be. 
    if isValidCard(check): #Checks if the input is a real card or not
        print("Valid.")
    else:
        print("Invalid.")

if __name__ == "__main__": #Script is being run as the main program
    main()