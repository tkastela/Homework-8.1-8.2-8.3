secret = 8

guess = int(input("Guess the secret number (between 1 and 10): "))

if guess == secret:
    print("You've guessed it. Congratulations! It's number 8.")
else:
    print("Sorry, your guess is not correct. The secret number is not " + str(guess))