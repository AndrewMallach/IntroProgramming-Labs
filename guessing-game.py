def main():

    print("PYTHON GUESSING GAME")
    
    answer = "cow"

    while True:
        guess = input("I am thinking of an animal. What animal am I thinking of?    ")
        if guess == answer:
            print("You win!")
            break

        else:
            print("Try again...")



main()
