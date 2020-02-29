'''
Created on Nov 23, 2019

@author: ITAUser
'''
#import the random library

#define a function called pick_random_word(): 
    #open and read word dictionary/list 
    
    #variable called index  = select random word from words.txt
    #variable called word = strip the randomly selected word 
    #return variable called 'word'
#define a function called ask_for_next_letter():
    #variable called letter = input function that asks user to select a letter 
    #return the letter selected
#define a function called generate_word_string(word, letters_guesssed):
    #variable called output = empty list
    #make a for loop that goes through each letter in the variable 'word':
        #if statement  that checks if letter is in letters guessed:
            #append letter to output
        #else:
            #append ("_")
        #return output as a string

#create a main module:
    #variable:called WORD = pick_random_word()
    
    #letters_to_guess = set of WORD
    #variable called correct_letters_guessed = empty set
    #variables called incorrect_letters_guessed = empty set 
    #variable called  number_of_guesses = number of guesses allowed
    
    #print statement that welcomes the user to hangman
    
    #while loop that runs until number_of guesses is greater than 1 or letters_to_guess is greater than 0
        #variable called guess = ask_for_next_letter() and turn into lower case
        
        #if statement that checks if guess is in correct_letters_guessed or guess in in incorrect_letters_guesed
            #print statement that says you already guessed that letter
        
        #if statement checks if guess is in letters_to_guess
            #remove guess from letters_to_guess
            #add guess to correct_letters_guessed
        #else:
            #add letters to incorrect_letters_guessed
            #number_of_guesses goes down by one
        #variable called word_string = generate_word_string(WORD, correct_letters_guessed)
        #print statement that prints word string
        #print statement that prints how many guesses you have left
        
        #if statement to check numbers of guesses is greater than a value;
            #print congratulations you guessed the word right 
        #else:
            #print sorry lost the word was WORD sssss1x
        
        
        