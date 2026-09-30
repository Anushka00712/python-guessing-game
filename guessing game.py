import random as rand

print("Welcome to my Guessing Game!!")

print("1. Easy (range 1-20)")
print("2. Medium (range 1-50)")
print("3. Hard (range 1-100)")

diff = input("Select a difficulty level: ").title()

def game(max_num):
    num = rand.randint(1,max_num)
    count = 0

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
            break

    print(f"You got it in {count} guesses")

if diff == "1" or diff == "Easy":
    game(20)
elif diff == "2" or diff == "Medium":
    game(50)
elif diff == "3" or diff == "Hard":
    game(100)
else:
    print("Invalid difficulty level")
