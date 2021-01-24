from replit import clear
from art import logo
import random

# each card symbol and score (list of tuples)
# assume ACE is 11 score
card_symbol = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_score = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_pair = list(zip(card_symbol, card_score))


# flip the card randomly (tuple)
def flip_nextcard(all_card_pair):
  choosed_card = random.choice(all_card_pair)
  return choosed_card

# update record boards
def update_records(choosed_card, current_symbols, current_scores):
  current_symbols.append(choosed_card[0])
  current_scores += choosed_card[1]
  return current_symbols, current_scores

# annouce current scores
def lastest_record(who, current_symbols, current_scores):
  current_symbols = ' , '.join(current_symbols)
  print(f"📣   {who}'s hand cards: [ {current_symbols} ], current score: {current_scores}")  

# # # Special Case: score > 21
# def trans_ACE(choosed_card, current_symbols, current_scores):
#   if choosed_card != 'A':
#     print("🅰  in HandCards. Change Score as below:")
#     get_score = 0
#     for symbol in current_symbols:
#       index = card_symbol.index(symbol)
#       if symbol == 'A':
#         get_score += 1
#       else:
#         get_score += card_score[index]
#     current_scores = get_score

#   elif choosed_card == 'A':
#     print("Flipped 🅰 Card. Change Score as below:")
#     current_scores = current_scores - 10
  
#   print(f"🅰 🔁  current score: {current_scores}")
#   return current_scores

# Special Case: current_score>21
def check_trans_ACE(current_symbols, current_scores):
  ace_card = current_symbols.count('A')
  if ace_card > 0:
    print("🅰 in HandCards. Change Score as below:")
    # calculate total score
    current_scores = 0
    for symbol in current_symbols:
      index = card_symbol.index(symbol)
      current_scores += card_score[index]
    # change ACE score from 11 to 1
    while ace_card > 0 and current_scores > 21:
      current_scores = current_scores - 10
      ace_card -= 1
    print(f"🅰 🔁  current score: {current_scores}")

  # check the score after changing
  if current_scores > 21:
    isWentOver = True
  else:
    isWentOver = False
  return isWentOver, current_scores




# GLOBAL Parameter
play_game = True
while play_game:
  # GLOBAL Parameter
  filp_compu_card = True
  user_filp_card = True
  isWentOver = False
  start = input("Do you want to play a Blackjack game of Blackjack? Type 'y' or 'n': ").lower()
  if start == 'y':
    # clear screen and show the logo
    clear()
    print(logo)

    # create user's and computer's record board
    user_current_symbols = []
    user_current_scores = 0
    comp_current_symbols = []
    comp_current_scores = 0

    # flip TWO cards to user (tuple of tuples)
    user_cards = flip_nextcard(card_pair), flip_nextcard(card_pair)
    # update the latest symbol and score
    for user_card in user_cards:
      user_current_symbols, user_current_scores = update_records(user_card, user_current_symbols, user_current_scores)
    # announce the lastest record 
    lastest_record("Gamer", user_current_symbols, user_current_scores)

    '''
    兩張都抽到AA
    '''
    if user_current_scores > 21:
      isWentOver, user_current_scores = check_trans_ACE(user_current_symbols, user_current_scores)
    
    # flip ONE card to computer
    comp_card1 = flip_nextcard(card_pair)
    comp_current_symbols, comp_current_scores = update_records(comp_card1, comp_current_symbols, comp_current_scores)
    # announce the lastest record 
    lastest_record("Computer", comp_current_symbols, comp_current_scores)

  # if user wants to stop the game(after the else blocks will NOT run)
  else:
    play_game = False
    break


  # user takes turn  
  while user_filp_card:
    again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if again == 'y':
      # filp the card randomly
      user_card = flip_nextcard(card_pair)
      # update the latest symbol and score
      user_current_symbols, user_current_scores = update_records(user_card, user_current_symbols, user_current_scores)
      # announce the lastest record 
      lastest_record("user", user_current_symbols, user_current_scores)
      lastest_record("Computer", comp_current_symbols, comp_current_scores)
      
      # Special Case
      if user_current_scores > 21:
        isWentOver, user_current_scores = check_trans_ACE(user_current_symbols, user_current_scores)
        
        if isWentOver:
          filp_compu_card = False
          break

    # user doesn't flip another card, it's computer's turn
    else:
      user_filp_card = False


  # computer takes turn 
  ## gamer stopped flipping a card or the score was over
  while filp_compu_card: 
    # filp the card randomly
    comp_card = flip_nextcard(card_pair)
    # update the latest symbol and score
    comp_current_symbols, comp_current_scores = update_records(comp_card, comp_current_symbols, comp_current_scores)
    
    # Special Case
    if comp_current_scores > 21:
      comWentOver, comp_current_scores = check_trans_ACE(comp_current_symbols, comp_current_scores)
      if comWentOver:
        # game over, cpu loose
        filp_compu_card = False

    # computer's score is more than user's score should stop
    if comp_current_scores > user_current_scores:
      filp_compu_card = False


  # final hand and score between user and computer
  user_current_symbols = ' , '.join(user_current_symbols)
  comp_current_symbols = ' , '.join(comp_current_symbols)
  if isWentOver:
    print("💥💥💥 You went over 💥💥💥. You lose 😤")
  else:
    print("-------------------- Final_Result ---------------------")
    print(f"  Your final hand: [ {user_current_symbols} ] \n🉐 Final score: {user_current_scores}")
    print(f"  Computer's final hand: [ {comp_current_symbols} ] \n🉐 Final score: {comp_current_scores}")

    # compare user's and computer's score
    if comp_current_scores <= 21:
      if user_current_scores < comp_current_scores :
        print("🔚  You Lose 😤")
      elif user_current_scores == comp_current_scores:
        print("🔚  It's Draw 🙃")  
      elif user_current_scores > comp_current_scores :
        print("🔚  You Win 😃")
    elif comp_current_scores > 21:
      if user_current_scores <= 21:
        print("🔚  You Win 😃")