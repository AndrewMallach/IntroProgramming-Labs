def main():

    print("PYTHON GUESSING GAME")
    
    answer = "orangutan"

    while True:
        guess = input("I am thinking of an animal. What animal am I thinking of?    ")
        normGuess = guess.strip().lower()
        if normGuess == answer:
            like = input("Do you like orangutans? Yes or no?   ")
            normLike = like.strip().lower()
            if normLike == "yes":
                print("Great!")
            elif normLike == "no":
                print("Aww :(")
                
        elif normGuess[0] == "q":
            break

        else:
            print("Try again...")



main()
