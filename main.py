from art import logo, vs
from game_data import data
import random

print(logo)

def format_data(account):
    name = account["name"]
    job = account["description"]
    country = account["country"]
    return f"{name}, a {job}, from {country}."

def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"

score = 0
end_game = False
account_b = random.choice(data)

while not end_game:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    followers_a_count = account_a["follower_count"]
    followers_b_count = account_b["follower_count"]

    is_correct = check_answer(guess, followers_a_count, followers_b_count)
    
    if is_correct:
        score += 1
        print(f"You got it right✨ Your current score is: {score}")
    else:
        end_game = True
        print(f"Sorry, that was wrong☹️  Your final score is: {score}")