#from blackjack import values
import Deck

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces_as_ten = 0    # add an attribute to keep track of aces
        self.aces_as_one = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += Deck.values[card.rank]
        if(card.rank=='Ace'):
          self.aces_as_ten+=1
          print('you have got ace!\n')
    
    def adjust_for_ace(self):

          if(self.aces_as_ten>0):
          	for i in range(self.aces_as_ten):
          		self.value-=10
          		self.aces_as_one+=1
          	self.aces_as_ten-=self.aces_as_one

          elif(self.aces_as_one>0):
          	for i in range(self.aces_as_one):
          		self.value+=10
          		self.aces_as_ten+=1
          	self.aces_as_one-=self.aces_as_ten

          