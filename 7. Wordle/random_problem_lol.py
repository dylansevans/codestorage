from valid_wordle_guesses import get_valid_wordle_guesses

words = get_valid_wordle_guesses()

good_words = set()

common_letters = {"A", "E", "R", "T", "O"}

# for word in words:
#     for letter in set(word):
#         try:
#             letter_counts[letter] += 1
#         except KeyError:
#             letter_counts[letter] = 1

# print(sorted(letter_counts.values()))
# print(letter_counts)

for word in words:
    if len(set(word) ^ common_letters) == 0: good_words.add(word)
    
print(good_words)