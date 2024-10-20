from art import logo
print(logo)
import random
#from art import logo
print("Welcome to the Number Guessing Game")
easy_level =10
hard_level=5

def choose_num():
    print("i am thinking about a number bw 1 to 100")
    num=random.randint(1,100)
    return num
def choose_difficulty():
    diff=input("Choose a difficulty level ie. easy or hard :").lower()
    if diff=="easy":
        print("you have 10 attemps")
        return easy_level
    elif diff=="hard":
        print("You have 5 attemps")
        return hard_level
    else:
        print("choose a valid difficulty")

    
def user_guess(num,turns_left):
    while turns_left>0:
        user_g=int(input("Make a guess:"))
        if user_g==num:
            print(f"your guess is right the answer is {num}")
            return "end game "
        elif user_g>num:
            print("Too High")
            
        else:
            print("TOO Low")
        turns_left-=1
        if turns_left>0:
            print(f"{turns_left} are left ")
        else:
            print("your out of attempts")
def game():
    num=choose_num()
    turns_left=choose_difficulty()
    user_guess(num,turns_left)
game()