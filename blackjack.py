import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,10,10,10,10]
    return random.choice(cards)
def calculate(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)        

user_card=[]
computer_card=[]
comp_score=-1
user_score=-1
is_game_over =False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card()) 
while not is_game_over:
    user_score=calculate(user_card)
    comp_score=calculate(computer_card)
    print(f"your cards are {user_card} , and score is {user_score}")
    print(f"computer cards are {computer_card[0]}")
    
    if user_score == 0 or comp_score==0 or user_score>21:
        is_game_over =True
    else:
        user_should_deal=input("type y to continue and press n to pass the card :")
        if user_should_deal=='y':
            user_card.append(deal_card())
        else:
            is_game_over=True
while comp_score<17 and comp_score!=0:
    computer_card.append(deal_card())
    comp_score=calculate(computer_card)

def compare(user_score,c_score):
    if user_score==c_score:
        return "Draw"
    elif c_score==0:
        return "you lost,opponent has blackjack"
    elif user_score==0:
        return "You Win with a blackjack"
    elif c_score>21:
        return "opponent went over 21 , you win"
    elif user_score>21:
        return "youlose went over 21"
    elif user_score>c_score:
        return "you win"
    else:
        return "you lose"

print(compare(user_score,comp_score))