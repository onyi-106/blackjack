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


#Starting cards
draw_card("player"), draw_card("player")
draw_card("dealer"), draw_card("dealer")


#Debugging
# draw_card("player")
print(blackjack_info)

print(f"Your cards: {access_cards('player')}, current score: {access_score('player')}")
print(f"Dealer's first card: {access_cards('dealer')[0]}")
direction = input("Type 'h' to hit, type 's' to stand:")

if direction == "h":
  draw_card("player")

