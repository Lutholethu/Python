import random
import art

card_selection = [11,2,3,4,5,6,7,8,9,10,10,10,10]

card_comp = (random.sample(card_selection, 2))
card_user = (random.sample(card_selection, 2))

card = (random.choice(card_selection))


#storing card selection in list
computer_cards = []
Your_cards = []
gameover = False

print(art.logo)
print(f"Your cards: {card_user}")
Your_cards.extend(card_user)

#stores the computer cards in a list and prints the first number
computer_cards.extend(card_comp)
print(f"Computer's first card: {computer_cards[0]}")

for numbers in computer_cards and Your_cards:
    total_comp = computer_cards[0] + computer_cards[1]
    total_user = Your_cards[0] + Your_cards[1]
    if total_comp == 21:
        print(f"computer is the winner. Cards: {computer_cards}")
    elif total_user == 21:
        print(f"User is the winner. Cards: {Your_cards}")


    while gameover == False:

        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            Your_cards.append(card)
            total_user = Your_cards[0] + Your_cards[1] + Your_cards[2]
            gameover = True

        else:
            gameover = True

        if total_comp < 17:
            computer_cards.append(card)
            total_comp = computer_cards[0] + computer_cards[1] + computer_cards[2]
        else:
            total_comp = computer_cards[0] + computer_cards[1]

        if total_user <= 21:
            print(f"You win, your final hand is: {Your_cards}. Total = {total_user}")
            print(f"computer lost! your final hand is: {computer_cards}. Total = {total_comp}")

        elif total_user > 21:
            print(f"You lost! Your final hand is: {Your_cards}. Total = {total_user} ")
            print(f"computer wins! your final hand is: {computer_cards}. Total = {total_comp}")

        elif total_comp > 21:
            print(f"computer lost! your final hand is: {computer_cards}. Total = {total_comp}")
            print(f"You win, your final hand is: {Your_cards}. Total = {total_user}")
        elif total_comp <= 21:
            print(f"computer wins! your final hand is: {computer_cards}. Total = {total_comp}")
            print(f"You lost! Your final hand is: {Your_cards}. Total = {total_user} ")
        elif total_comp == total_user:
            print("its a draw!")

    if input("Do you want to play again? (y/n)") == 'y':
        Your_cards.clear()
        computer_cards.clear()
        