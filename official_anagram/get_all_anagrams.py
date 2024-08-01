import pickle
import time

dictionary = {}

with open('tuple_wordlist.txt', 'rb') as handle:
    dictionary = pickle.load(handle)

find_anagrams_word = "aabccdeefhijklmopqrsssttuvwxyz"
anagrams = set()

start_time = time.perf_counter_ns()

def branch_next(branch, rest_of_word):
    length = len(rest_of_word)
    for x in range(length):
        let = rest_of_word[x]
        if let in branch:
            if branch[let]["end"]:
                anagrams.add(branch[let]["end"])
            if length != 1:
                branch_next(branch[let], rest_of_word[:x] + rest_of_word[x + 1:])

branch_next(dictionary, find_anagrams_word)

end_time = time.perf_counter_ns()

print(anagrams)
print()
print(f"Length is {len(anagrams)}\n")
print(f"Finishes in {round((end_time - start_time) / 1000000, 4)}ms")