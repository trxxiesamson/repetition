# Program 1: 
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 

print("Welcome to Word Counter Simulator\n")
print("\nthis program allows you to input a phrase or sentence that you want to count the vowels, consonants, and even the words\n")

user_input = input("\nEnter a sentence that you want to evaluate: ")

vowel = 0
consonant = 0
special_char = 0
words = 1

for x in user_input:
    if(x == 'A'or x == 'E'or x == 'I'or x == 'O'or x == 'U' or
       x == 'a'or x == 'e'or x == 'i'or x == 'o'or x == 'u'):
        vowel = vowel + 1

    elif(x == 'B' or x == 'C' or x == 'D' or x == 'F' or x == 'G' or x == 'H' or 
    x == 'J' or x == 'K' or x == 'L' or x == 'M' or x == 'N' or x == 'P' or x == 'Q' or x == 'R' or
    x == 'S' or x == 'T' or x == 'V' or x =='W' or x == 'X' or x == 'Y' or x == 'Z' or x == 'a' or
    x == 'c' or x == 'd' or x == 'f' or x == 'g' or x == 'h' or x == 'j' or x == 'k' or x == 'l'
     or x == 'm' or x == 'n' or x == 'p' or x == 'q' or x == 'r' or x == 's' or x == 't' or x == 'v'
     or x == 'w' or x == 'x' or x == 'y' or x == 'z'):
        consonant = consonant + 1

    else:
        special_char = special_char + 1

for i in range(len(user_input)):
    if(user_input[i]==' ' or user_input == '\n' or user_input == '\t'):
        words=words+1

print("The passage contains the following number of vowels: ", vowel)
print("The following number of consonants appear in the text: ",consonant)
print ("The text contains the following number of special characters: ",special_char)
print("And the total amount of words in the particular text is: ", words)