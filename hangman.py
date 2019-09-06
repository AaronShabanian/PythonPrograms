#Hangman game

#make a list of words to draw from
words=["girl","school","boy","dog","women","men","university","chapman","sdsu","ucla"]
#randomly choose a word
import random
index = random.randint(0,len(words)-1)
answer = words[index]

puzzle=[]
for letter in answer:
    puzzle.append("-")

bad_guess=7
bad=0
i=0

complete=0
guess=[]
while(bad<7 and complete<len(answer)):
    print("".join(puzzle))
    g=0
    j=0
    letter=input("Enter letter guess ").lower()
    if letter.isalpha():
        k=0
        valid=0
        stopper=0
        while k<len(guess):
            if (letter==guess[k]) and (stopper==0):
                print("You have aready guessed this letter")
                valid=valid+1
                g=1
                stopper=stopper+1
            k=k+1
        while (j<len(answer)):
            length=len(guess)
            if valid==0:
                if letter==answer[j]:
                    g=1
                    complete=complete+1
                    puzzle[j]=letter
            j=j+1
        if (g==0):
            bad=bad+1
        guess.append(letter)
        print("You have used ",bad," bad guesses")
        print("Your Guesses: ","".join(guess))
    else:
        print("You must enter a letter ")
        bad=7
if bad==7:
    print("You Loose")
    print("""
     ______
     |     0
     |    \|/
     |     |
     |    / \
    _|_
    """)
else:
    print("".join(puzzle))
    print("""
    Y
    O
    U

    W
    I
    N
    """)
