import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0

def print_final_results(player_cards, player_score, dealer_cards, dealer_score, message):
  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {dealer_cards}, Computer's score: {dealer_score}")
  print(f"{message}")

def print_interim_results(player_cards, player_score, dealer_cards):
  print(f"Your cards: {player_cards}, current score: {player_score}")
  print(f"The dealer's first card is [{dealer_cards[0]}]")

def ask_user(player_score, dealer_score):
  response = input("Type 'y' to get another card, type 'n' to pass: ")
  if response == 'y':
    player_card = random.choice(cards)
    player_cards.append(player_card)
    player_score = sum(player_cards)

    dealer_card = random.choice(cards)
    dealer_cards.append(dealer_card)
    dealer_score = sum(dealer_cards)
    
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"The dealer's first card is [{dealer_cards[0]}]")

    if (player_score > 21 and dealer_score > 21) or (player_score == dealer_score):
      print_final_results(player_cards, player_score, dealer_cards, dealer_score, "It's a draw.")
    elif player_score > 21:
      if 11 in player_cards:
        if player_score - 10 > 21:
          print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You lost 😭.")
        else: 
          index = player_cards.index(11)
          player_cards[index] = 1
          print_interim_results(player_cards, player_score, dealer_cards)
          ask_user(player_score, dealer_score)
      else:
        print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You lost 😭.")
    elif dealer_score > 21:
      print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You won.")

  elif response == 'n':
    while dealer_score < 16:
      dealer_card = random.choice(cards)
      dealer_cards.append(dealer_card)
      dealer_score = sum(dealer_cards)
    
    if dealer_score > 21 or player_score > dealer_score:
      print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You won.")
    elif dealer_score > player_score:
      print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You lose 😤.")
    elif player_score == dealer_score:
      print_final_results(player_cards, player_score, dealer_cards, dealer_score, "It's a draw.")


response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if response == 'y':
  player_card1 = random.choice(cards)
  player_card2 = random.choice(cards)
  dealer_card1 = random.choice(cards)
  dealer_card2 = random.choice(cards)
  
  player_cards.append(player_card1)  
  player_cards.append(player_card2)
  dealer_cards.append(dealer_card1)  
  dealer_cards.append(dealer_card2)
  player_score = sum(player_cards)
  dealer_score = sum(dealer_cards)

  if dealer_score == dealer_score == 21:
    print_final_results(player_cards, player_score, dealer_cards, dealer_score, "It's a draw.")
  elif dealer_score == 21:
    print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You lost 😭.")
  elif dealer_score == 21:
    print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You won.")
  else:
    if player_score > 21:
      if 11 in player_cards:
        if player_score - 10 > 21:
          print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You lost 😭.")
        else: 
          index = player_cards.index(11)
          player_cards[index] = 1
          print_interim_results(player_cards, player_score, dealer_cards)
          ask_user(player_score, dealer_score)
      else:
        print_final_results(player_cards, player_score, dealer_cards, dealer_score, "You lost 😭.")
    else:
      print_interim_results(player_cards, player_score, dealer_cards)
      ask_user(player_score, dealer_score)
