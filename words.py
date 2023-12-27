def can_form_word(letters, word):
# Convert the letters and word to sets for easy comparison
letter_set = set(letters.lower())
word_set = set(word.lower())
# Check if the word can be formed using the given letters
return word_set.issubset(letter_set)
# Given list of words
word_list = ["Arun", "Varun", "Kent", "Eat", "Pot", "net", "Peak", "Peacock", "Zebra",
"Nato", "Toe", "Poke", "Knife", "Peot", "Venus", "Ant"]
# Letters to check against
letters_to_use = "AKEOTPN"
# Find and print the words that can be formed
valid_words = [word for word in word_list if can_form_word(letters_to_use, word)]
print("Words that can be formed with the letters:", valid_words)
