import random
import Card
from Deck import Deck
from Hand import Hand
from Chips import Chips

#execute the program
while(True):
  run_game()
  break


def hit(deck,hand):
    hand.add_card(deck.deal())
    #hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    while(True):
      print('Overall: {}'.format(hand.value))
      adjust_aces = input("\nDo you want adjust aces? 'y' or 'n' ")
        
      if(adjust_aces=='y'):
       hand.adjust_for_ace()
      
      player_move = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
      player_move.lower()


      if(player_move=='h'):
        hit(deck, hand)
        keep_playing=True

      elif player_move == 's':
        print("\nPlayer stands. Dealer is playing.")
        keep_playing = False

      else:
        print("Sorry, please try again.")
        continue
      return keep_playing


def show_some(player,dealer):
    
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer value: ",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("palyer value: ",player.value)
    

def player_busts(player,dealer,chip):
    print('Player busts!\n')
    chip.lose_bet()

def player_wins(chip):
    print('Player wins!\n')
    chip.win_bet()

def dealer_busts(player,dealer,chip):
    print('Dealer busts!\n')
    chip.win_bet()
    
def dealer_wins(chip):
    print('Dealer wins!\n')
    chip.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break



def run_game():

  player_chips = Chips()

  while True:
    #Print an opening statement
    print("Welcome to BlackJack!\nGet as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.\n\nYour stack is: {}".format(player_chips.total))
    take_bet(player_chips)

    deck = Deck()
    deck.shuffle()

    dealer_hand = Hand()
    player_hand = Hand()

    for i in range(2):
      dealer_hand.add_card(deck.deal())
      player_hand.add_card(deck.deal())

    show_some(player_hand, dealer_hand) # Show cards (but keep one dealer card hidden)
    keep_playing=True
    while (keep_playing):  # recall this variable from our hit_or_stand function

       keep_playing=hit_or_stand(deck, player_hand)
       print("keep_playing: {}\n".format(keep_playing))
       show_some(player_hand, dealer_hand) # Show cards (but keep one dealer card hidden)

       # If player's hand exceeds 21, run player_busts() and break out of loop
       if player_hand.value>21 :       
          player_busts(player_hand, dealer_hand, player_chips)
          break

    if player_hand.value <= 21:
        
        while dealer_hand.value <= 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()

           # Inform Player of their chips total    
    print("\nYour current stack: {}\n".format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        keep_playing=True
        continue
    else:
        print("Thanks for playing!")
        break
