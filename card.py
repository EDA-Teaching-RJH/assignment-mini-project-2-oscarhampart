class Card:
    def __init__(self, suit, rank): #Initialises card suit and rank
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}" #Returns a string that the user can read to know what their card is. 