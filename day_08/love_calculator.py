# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

# 2. Then check for the number of times the letters in the word LOVE occurs.

# 3. Then combine these numbers to make a 2 digit number and print it out.

word1 = "TRUE"
word2 = "LOVE"


def calculate_love_score(name1, name2):
    true_score = check_words(name=name1, word=word1) + check_words(name=name2, word=word1)
    love_score = check_words(name=name1, word=word2) + check_words(name=name2, word=word2)
    print(f"{true_score}{love_score}")


def check_words(name, word):
    return sum(1 for letter in name.upper() if letter in word)


calculate_love_score("Camila Montiel", "Lucas Neves")
