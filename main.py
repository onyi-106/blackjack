############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from art import logo

print(logo)

#1. MAKE THE ACTION CODE (HIT/STAND) IN A WHILE LOOP
#1.a. IF THE PLAYER WENT OVER 21 IMMEDIATELY LOSE
def blackjack():
  player_cards = []
  player_cards_summed = 0
  
  dealer_cards = []
  dealer_cards_summed = 0

  
  def draw_card():
    draw = random.choice(cards)
    return draw


#! INSTEAD OF DIVIDING BETWEEN THE PLAYER AND THE DEALER STARTING CARDS JUST PUT THEM INSIDE A DICTIONARY
  #PLAYER STARTING CARDS
  player_starting_deck = [draw_card(), draw_card()]
  player_cards.extend(player_starting_deck)
  player_cards_summed = sum(player_cards)
  print(f"Your cards: {player_cards}, current score: {player_cards_summed}")
  
  #DEALER STARTING CARDS
  dealer_starting_deck = [draw_card(), draw_card()]
  dealer_cards.extend(dealer_starting_deck)
  # dealer_cards_summed = sum(dealer_cards)
  print(f"Dealer's first card: {dealer_cards[0]}")
  
  def player_turn():
    is_hit = False
    while not is_hit:
      action = input("Type 'h' to HIT, type 's' to STAND: ")
      if action == "h":
        player_cards.append(draw_card())
        player_cards_summed = sum(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_cards_summed}")
        print(f"Dealer's first card: {dealer_cards[0]}")
    
    #2.DEALER TURNS IS EXECUTED AFTER PLAYER DECIDED TO STAND, IF PLAYER WENT OVER 21 AFTER DECIDING TO HIT, SKIP THE DEALER TURNS (return), AND IMMEDIATELY DECLARE THE RESULTS.
    
        if player_cards_summed > 21:
          is_hit = True
          player_loss = True
          # print("You went over. You lose lol")
          return
#IF THE PLAYER WENT OVER 21 THE GAME ENDS HERE.
      else:
        is_hit = True

  player_turn()
    
  #DEBUGGING
  # print(player_cards)
  # print(dealer_cards)

  ##DEALER'S TURN##  
  #IF DEALER'S SCORE IS HIGHER THAN THE PLAYER THEN ITS A LOSS FOR PLAYER.
  while dealer_cards_summed < 17:
    dealer_cards.append(draw_card())
  
  dealer_cards_summed = sum(dealer_cards)
  player_cards_summed = sum(player_cards)  
  if dealer_cards_summed > player_cards_summed:
    player_loss = True
  else:
    player_loss = False

  

  print(f"Your final hand: {player_cards}, final score: {player_cards_summed}")
  print(f"Computer's final hand: {dealer_cards}, final score: {dealer_cards_summed}")

  if player_loss:
    print("You Lose")
    



blackjack()

#FINAL HAND

