import pickle
import time
from valid_anagame_words import get_valid_word_list

dictionary = {}

with open('tuple_wordlist.txt', 'rb') as handle:
    dictionary = pickle.load(handle)

find_anagrams_word = "ewoiheg"


def handle(input_list):
    anagrams = set()
    branch_next(dictionary, ''.join(input_list), anagrams)
    return anagrams


start_time = time.perf_counter_ns()

def branch_next(branch, rest_of_word, anagrams):
    length = len(rest_of_word)
    for x in range(length):
        let = rest_of_word[x]
        if let in branch:
            if branch[let]["end"] and len(branch[let]["end"]) > 2:
                anagrams.add(branch[let]["end"])
            if length != 1:
                branch_next(branch[let], rest_of_word[:x] + rest_of_word[x + 1:], anagrams)


anagrams_set = handle(find_anagrams_word)


has_anagrams = set()

def prime_hash(word: str):
      prime_map = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
      'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
      'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
      'w': 83, 'x': 89, 'y': 97, 'z': 101 }
      #calculates the prime hash value for a given word
      hash_value = 1
      for letter in word:
        hash_value *= prime_map[letter]
      return hash_value

dictionary_keyed = {}

for word in get_valid_word_list():
    key = prime_hash(word)
    dictionary_keyed[key] = dictionary.get(key, []) + [word]

def add_new_letter(word, length_left):
    for let_num in range(97, 122):
        letter = chr(let_num)
        new_letter = word + letter
        if length_left != 1:
            add_new_letter(new_letter, length_left - 1)
        else:
            anagrams = handle(new_letter)
            has_anagrams = set()
            for wordK in list(anagrams):
                key = prime_hash(wordK)
            if len(dictionary_keyed[key]) > 1:
                has_anagrams = has_anagrams.union(dictionary_keyed[key])
            if len(has_anagrams) > 1:
                return new_letter
        ### END SOLUTION


print(add_new_letter("", 7))


end_time = time.perf_counter_ns()



print(anagrams_set)
print()
print(f"Length is {len(anagrams_set)}\n")
print(f"Finishes in {round((end_time - start_time) / 1000, 4)} microseconds")