import random
from art import logo,vs
from game_data import data

user_points = 0
is_game_over = False
item1 = random.choice(data)
item2 = random.choice(data)

while not is_game_over :
    print(logo)
    print(f"name: {item1['name']}, country: {item1['country']}, description: {item1['description']}")
    print(vs)
    print(f"name: {item2['name']}, country: {item2['country']}, description: {item2['description']}")

    follower_count1 = item1['follower_count'] 
    follower_count2 = item2['follower_count']

    choice = input(f"Choose between 'A' and 'B': ").upper()

    if choice == 'A' and follower_count1 > follower_count2:
        print("Great job! Option 'A' is the correct answer.")
        user_points += 1
        print(f"You have: {user_points} points")
        item2 = random.choice(data)

    elif choice == 'B' and follower_count1 > follower_count2:
        print("Option 'B' is incorrect. GameOver!")
        is_game_over = True

    elif choice == 'B' and follower_count1 < follower_count2:
        print(" Great job! Option 'B' is the correct answer.")
        user_points += 1
        print(f"You have: {user_points} points")
        item1 = item2
        item2 = random.choice(data)

    else:
        print("Option 'A' is incorrect. GameOver!")
        is_game_over = True



