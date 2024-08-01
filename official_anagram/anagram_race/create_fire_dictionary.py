import pickle
from valid_anagame_words import get_valid_word_list

dictionary = {}

def add_letter(current_directory, rest_of_word, full_word):
    first_letter = rest_of_word[0]
    if first_letter in current_directory:
        if len(rest_of_word) == 1:
            current_directory[first_letter]["end"] = (True, full_word)
        else:
            add_letter(current_directory[first_letter], rest_of_word[1:], full_word)
    else:
        current_directory[first_letter] = {"end": False}
        if len(rest_of_word) == 1:
            current_directory[first_letter]["end"] = full_word
        else:
            add_letter(current_directory[first_letter], rest_of_word[1:], full_word)



def main():
    for word in get_valid_word_list():
        add_letter(dictionary, word, word)

main()

# with open("tuple_wordlist.txt", "wb") as f:
#     pickle.dump(dictionary, f)