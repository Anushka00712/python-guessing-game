import random as rand

num = rand.randint(1,100)
count = 0

while True:
    try:
        guess = int(input("Guess:"))
        if guess<1 and guess>100:
            print("Please enter a number in between 1 and 100")
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
