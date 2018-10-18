def main():

    print("PYTHON GUESSING GAME")
    
    answer = "cow"

    while True:
        guess = input("I am thinking of an animal. What animal am I thinking of?    ")
        normGuess = guess.strip().lower()
        if normGuess == answer:
            print("You win!")
            break
        elif normGuess == "quit":
            break

        else:
            print("Try again...")



main()
