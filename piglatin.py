# Evan Sauers
# piglatin.py
# Week 3: Pig Latin Assignment

# This program translates words to Simple Pig Latin.

word = input("Enter an English word to translate into Simple Pig Latin: ")        # Prompt the user to enter an English word to translate
   
vowel = "aeiou"
	
if word[0] in vowel:        #Calculate the word
    print(word + "yay")
else:
    print(word[1:] + word [0] + "ay")        #Print results
        
