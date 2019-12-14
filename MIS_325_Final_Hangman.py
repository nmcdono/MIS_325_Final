# This program is allows two players to play a game of hangman
print("Hangman\nThis game will take an imput from a user for the game to be played by another")
# uppercase input word from the first user for the game
word = str(input("Please input a word to for another user to play: "))
word = word.upper()
# print spacing to prevent cheating
print("***\n" * 20)
# Graphical output for the game
HANGMAN_GRAPHIC = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

# Primary game while loop
loop=1
while loop==1:
    blank='-' * len(word)  
    wrong=-1   
    correct=[]
    
    user_letters=[]

# function to take user guesses and catch errors in input
    def guesses():
        print()
        guess=input("Please input a letter: ")
        guess=guess.upper()
        print() 
# if elif and else statments to correct repeated inputs, multiple inputs, non letter inputs
        if guess in user_letters:
            print(guess + " was already tried, please input a new letter: ")
            guesses()
        elif len(guess) !=1:
            print("Please input only one letter at a time")
            guesses()
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print("input letters only")
            guesses()
        else:
            user_letters.append(guess)
        return guess

# while loop to setup blank outputs
    running=True
    while running==True: 
        correct=[]  
        for x in range(len(word)):
           if word[x] in user_letters:
                blank=blank[:x] + word[x] + blank[x+1:]                
                correct.append(x)

# spacing inbetween guesses
        print("\n" * 7)
# if else to print the same or next guess

        if wrong < 5:
            print(HANGMAN_GRAPHIC[wrong+1])
        else:
            print(HANGMAN_GRAPHIC[wrong+1])
            print()
            print("You Have lost")
            running=False

# if statement for victory
        if len(correct)==len(word):
            print()
            print("You Have Won!")
            running=False

# print blanks
        print()
        print( blank + "") 
        print()
        print( end='')
     
        for x in range(len(user_letters)):
             print(end='')
             print(user_letters[x], end='')

# advance game if guess is incorrect
        guess=guesses()   
        if not guess in word:
            wrong=wrong+1
           