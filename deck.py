import random #Importing random so the cards chosen are random and so the deck can be shuffled 
from card import Card #Importing the cards

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank)) #This makes the whole deck of the 52 cards, giving each suit every rank. 

    def shuffleDeck(self):
        random.shuffle(self.cards) #Shuffles the cards so they are random

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop() #Card is popped so can't be reused after dealt. 
        return None