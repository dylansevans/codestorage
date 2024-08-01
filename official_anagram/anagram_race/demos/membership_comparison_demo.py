import time
from valid_anagame_words import get_valid_word_list # only words with 2 - 7 letters

all_words_list = get_valid_word_list()
print(f"word_list is a {type(all_words_list)} with {len(all_words_list)} words in it.")

all_words_set = set()
for word in all_words_list:
    all_words_set.add(word)
print(f"all_words_set is a {type(all_words_set)} with {len(all_words_set)} words in it.")

input=["abacus", "begin", "middle", "night", "yellow", "zoom", "gjdhddsjg"]
word_collections=[all_words_list, all_words_set]

for word in input:
    print(f"{word}:")
    for collection in word_collections:
        start = time.perf_counter()
        if word in collection:
            stop = time.perf_counter()
            elapsed_time = (stop-start)*1000

            print(f'\tIt took {round(elapsed_time,5)}s to find "{word}" in a {type(collection)}')
        else:
            stop = time.perf_counter()
            elapsed_time = (stop-start)*1000

            print(f'\tIt took {round(elapsed_time,5)}s to find out that "{word}" is not present in a {type(collection)}')
