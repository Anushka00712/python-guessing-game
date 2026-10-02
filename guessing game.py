import random

def main_menu():
    print("Welcome to my Guessing Game!!")

    print("1. Easy (range 1-20)")
    print("2. Medium (range 1-50)")
    print("3. Hard (range 1-100)")
    diff = input("Select a difficulty level: ").title()

    return diff

def game(max_num,max_guesses):
    num = random.randint(1,max_num)
    count = 0
    won = False

    while True:
        try:
            guess = int(input("Guess: "))

            if guess <1 or guess>max_num:
                print(f"Please enter a number in between 1 and {max_num}")
                continue

        except ValueError:
            print("Please enter a number")
            continue

        if guess>num:
            print("Too High")
            count +=1
        elif guess<num:
            print("Too Low")
            count+=1
        else:
            print("Correct!!")
            count +=1
            won = True
            break

        if count>=max_guesses:
            print("You have run out of guesses :(")
            print(f"The number was {num}!")
            break

    if won:
        print(f"You got it in {count} guesses!!")

def replay():
    while True:
        answer = input("Would you like to play again? (y/n): ").lower().strip()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please put valid input y/n")

while True:

    diff = main_menu()

    if diff == "1" or diff == "Easy":
        game(20,5)
    elif diff == "2" or diff == "Medium":
        game(50,6)
    elif diff == "3" or diff == "Hard":
        game(100,8)
    else:
        print("Invalid difficulty level")
        continue

    if replay():
        continue
    else:
        print("Thank you for playing!!")
        break
