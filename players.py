class Player: #Player class which has a name, balance and their own hand, each players gets these. This is the super class
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = [] #Each player will have 2 cards

class User(Player): #This is the user player class
    def __init__(self, name, balance, position):
        super().__init__(name, balance) #This is a sub class that inherited the super classes traits
        self.position = position #Indicates who goes first, the user or the AI, as it would be unfair for the same player to go first every time. 

class AI(Player): #This is the AI player class
    def __init__(self, name, balance, difficulty):
        super().__init__(name, balance) #This is a sub class that inherited the super classes traits
        self.difficulty = difficulty #Difficulty of the AI which will be able to be changed. 