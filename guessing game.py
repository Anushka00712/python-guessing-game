import random as rand

num = rand.randint(1,100)
count = 0

while True:
    guess = int(input("Guess:"))
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
