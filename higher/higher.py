import random
from art1 import logo,logo1
#print(logo)

celebrities = [
    {
        "name": "Cristiano Ronaldo",
        "followers": 620_000,
        "description": "Footballer, athlete, icon",
        "country": "Portugal"
    },
    {
        "name": "Taylor Swift",
        "followers": 450_000,
        "description": "Singer, songwriter, superstar",
        "country": "USA"
    },
    {
        "name": "Kim Kardashian",
        "followers": 350_000,
        "description": "Reality star, entrepreneur",
        "country": "USA"
    },
    {
        "name": "Lionel Messi",
        "followers": 500_000,
        "description": "Footballer, legend, icon",
        "country": "Argentina"
    },
    {
        "name": "Dwayne \"The Rock\" Johnson",
        "followers": 360_000,
        "description": "Actor, wrestler, icon",
        "country": "USA"
    },
    {
        "name": "Ariana Grande",
        "followers": 390_000,
        "description": "Singer, actress, icon",
        "country": "USA"
    },
    {
        "name": "Selena Gomez",
        "followers": 420_000,
        "description": "Actress, singer, producer",
        "country": "USA"
    },
    {
        "name": "Virat Kohli",
        "followers": 260_000,
        "description": "Cricketer, captain, icon",
        "country": "India"
    },
    {
        "name": "Kylie Jenner",
        "followers": 395_000,
        "description": "Entrepreneur, media personality",
        "country": "USA"
    },
    {
        "name": "Shakira",
        "followers": 240_000,
        "description": "Singer, dancer, philanthropist",
        "country": "Colombia"
    },
    # New Celebrities
    {
        "name": "Billie Eilish",
        "followers": 300_000,
        "description": "Singer, songwriter, icon",
        "country": "USA"
    },
    {
        "name": "LeBron James",
        "followers": 320_000,
        "description": "Basketball, athlete, legend",
        "country": "USA"
    },
    {
        "name": "Justin Bieber",
        "followers": 350_000,
        "description": "Singer, pop star",
        "country": "Canada"
    },
    {
        "name": "Priyanka Chopra",
        "followers": 280_000,
        "description": "Actress, global icon",
        "country": "India"
    },
    {
        "name": "Zendaya",
        "followers": 330_000,
        "description": "Actress, singer, star",
        "country": "USA"
    }
]
def get_celeb():
    A= random.choice(celebrities)
    B= random.choice(celebrities)
    while A==B:
        B=random.choice(celebrities)
    return A,B
def higher_lower():
    score=0
    game_over=False

    while not game_over:
        A,B=get_celeb()
        print(f"Compare A: {A["name"]}, {A["description"]},from {A["country"]}")
        print(logo1)

        print(f"Against B: {B["name"]}, {B["description"]},from {B["country"]}")
        score=0
        guess=input("Who has more followers ? Type 'A' or 'B': ").lower()
        if check_answer(guess,A,B):
            score+=1
            print(f"your right  CUrrent score is {score}")
        else:
            game_over=True
            print(f"you lose man ")
def check_answer(guess,A,B):
    if guess == 'a' and A['followers'] > B['followers']:
        return True
    elif guess == 'b' and B['followers'] > A['followers']:
        return True
    else:
        return False
higher_lower()