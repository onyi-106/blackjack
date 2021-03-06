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

blackjack_info = {
  "player": {"cards": [], "score": 0},
  "dealer": {"cards": [], "score": 0}
}
#Function to access dealer / player cards
def access_cards(person):
  """person = player/dealer"""
  return blackjack_info[person]["cards"]
  
#Function to access dealer / player score
def access_score(person):
  """person = player/dealer"""
  return blackjack_info[person]["score"]
  
#To draw card
def draw_card(person):
  access_cards(person).append(random.choice(cards))
  def sum_card():
    blackjack_info[person]["score"] = sum(access_cards(person))
  sum_card()

#Play game function IMPORTANT
  #Starting cards
def play_game():
  draw_card("player"), draw_card("player")
  draw_card("dealer"), draw_card("dealer")
  
  
  #Debugging
  # draw_card("player")
  print(blackjack_info)
  
    
  over = False
  while not over:
    print(f"Your cards: {access_cards('player')}, current score: {access_score('player')}")
    print(f"Dealer's first card: {access_cards('dealer')[0]}")
  #Ask the player
    direction = input("Type 'h' to hit, type 's' to stand:")
    if direction == "h":
      draw_card("player")
      #If the player score went over 21 its a BUST'
      if access_score("player") > 21:
        over = True
        print(f"Your final hand is {access_cards('player')} final score: {access_score('player')}")
        print(f"Dealer's final hand: {access_cards('dealer')}, final score: {access_score('dealer')}")
        
        print("You went over, you lose.")
        return
    else:
      over = True
      #While dealer score is under 17, keep drawing card.
  while access_score("dealer") < 17:
    draw_card("dealer")
    #If the dealer score went over 21, DEALER BUST.
    if access_score("dealer") > 21:
      # return "dealer_bust"
      print(f"Your final hand is {access_cards('player')} final score: {access_score('player')}")
      print(f"Dealer's final hand: {access_cards('dealer')}, final score: {access_score('dealer')}")

      print("Dealer went over, you win.")
      return
  #While the dealer score is more than 17 and doesnt exceed 21 then proceed to calculation on which has the higher score.

  #Won by higher score
  if access_score("player") > access_score("dealer"):
    print(f"Your final hand is {access_cards('player')} final score: {access_score('player')}")
    print(f"Dealer's final hand: {access_cards('dealer')}, final score: {access_score('dealer')}")

    print("You win")
    return
  #Lose by lower score
  else:
    print(f"Your final hand is {access_cards('player')} final score: {access_score('player')}")
    print(f"Dealer's final hand: {access_cards('dealer')}, final score: {access_score('dealer')}")

    print("You lose!!")
    return
  

#Calling the game function:
play_game()