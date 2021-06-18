import random


def guess(x):
    rand = random.randint(1, x)
    guess = 0
    while guess != rand:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < rand:
            print("Sorry,guess again, too low!!")
        elif guess > rand:
            print("Sorry,guess again, too high!!")
    print("Congrats, you have guess the number correctly!!!")


guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H) , too low(L), or correct(C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print("yay! the computer guess your number correctly!!!!")


computer_guess(10)