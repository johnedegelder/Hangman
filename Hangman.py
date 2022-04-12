
# Open hangman.txt
f = open("hangman.txt", "r")  # r opens the file in "read" mode
hangmanword = (f.read())  # prints the contents of the file
f.close()
print(hangmanword)

# Splice hangman word into a list, Thanks SJ :)
letterlist = list(hangmanword)
wrongletterlist = []

print(letterlist)
displaylist = []  # used to display _ and guessed letter to the player
for i in letterlist:  # adds amount of _ for letter in the word
    displaylist.append("_")

def wrongletter(i,j):
    global score
    if j == 0:
        global wrongletterlist
        wrongletterlist.append(i)
        print(wrongletterlist)
        score = score +1
    else:
        print("good work")

def letterguess():  # takes player input and updates disaply list if guess was correct
    global letterlist
    guess = input("Please guess a letter : ")
    counter = 0
    j = 0
    for i in letterlist:
        if guess == i :
            displaylist.pop(counter)
            displaylist.insert(counter,guess)
            counter = counter +1
            j = 1
        else:
            counter = counter +1
    wrongletter(guess,j)

lives = 5
score = 0
from hangmanpics import HANGMANPICS
while True:
    letterguess()
    print(displaylist)
    print(wrongletterlist)
    l = lives - len(wrongletterlist)
    print(HANGMANPICS[score])
    if len(wrongletterlist) > 0:
        print("You have " + str(l) + " wrong letters left TILL YOU\'LL DIE")
    if "_" not in displaylist:
        print("YOU WIN!!!")
        break




