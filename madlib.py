def promptForWords():
    global noun,verb,adj,place
    noun = input ("Enter a noun ")
    verb = input ("Enter a verb ")
    adj = input ("Enter an adjective ")
    place = input ("Enter a place ")

def makeAndPrintSentence():
    print("Take your " + adj + " " + noun + " and " + verb + " it at the " + place + "!")

def madlib():
    promptForWords()
    makeAndPrintSentence()

madlib()
