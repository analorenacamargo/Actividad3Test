#palabra o frase es palindromo
# Ask the user to input a word or phrase
word = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase for uniform comparison
word = word.replace(" ", "").lower()

# Reverse the word or phrase
reversed_word = word[::-1]

# Check if the original word is the same as the reversed word
if word == reversed_word:
    print(f"The word or phrase '{word}' is a palindrome.")
else:
    print(f"The word or phrase '{word}' is not a palindrome.")
