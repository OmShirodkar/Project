import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n\
    "Rock vs Paper -> Paper wins \n\
    "Rock vs Scissors -> Rock wins \n\
    "Paper vs Scissors -> Scissor wins \n\
')

while True:
    choice = int(input("Enter your choice (1 for Rock / 2 for Paper / 3 for Scissors): "))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please: '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is', choice_name)
    print('Now its Computers Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    
    print("Computer choice is", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('It\'s a Draw!')
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print('Computer wins!')
        result = 'Computer'
    else:
        print('You win!')
        result = 'User'

    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing")
