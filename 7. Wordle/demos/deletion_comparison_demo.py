import time
from valid_wordle_guesses import get_valid_wordle_guesses # only words with 2 - 7 letters

all_words_list = sorted(get_valid_wordle_guesses())
print(f"word_list is a sorted {type(all_words_list)} with {len(all_words_list)} words in it.")

all_words_set = set()
for word in all_words_list:
    all_words_set.add(word)
print(f"all_words_set is a {type(all_words_set)} with {len(all_words_set)} words in it.")

input=["ABYSS", "BEGIN", "MOMMY", "NIGHT", "YUMMY", "ZORRO"]
word_collections=[all_words_list, all_words_set]

trials = 100
data=[]
for word in input:
    new_row=[word]
    print(f"{word}:")
    for collection in word_collections:
        #----Membership-----#
        start = time.perf_counter()
        for t in range(trials):
            if word in collection:
                pass
        stop = time.perf_counter()
        avg_membership_time = ((stop-start))/trials*1000
        new_row.append(avg_membership_time)
        print(f'\tIt took an average of {format(avg_membership_time,"0.5f")}s to find "{word}" in a {type(collection)}')
        
        #----Remove-----#
        # Note: list.remove must search the list for the index first, then removes the element
        #       This is why it appears that removing from the end of the list takes longer
        total_time=0
        for t in range(trials):
            words_copy = collection.copy()
            start = time.perf_counter()
            words_copy.remove(word)
            elapsed_time = time.perf_counter()-start
            total_time = total_time + elapsed_time
        avg_remove_time = total_time/trials*1000
        new_row.append(avg_remove_time)

        print(f'\tIt took an average of {format(avg_remove_time,"0.8f")}s to remove "{word}" from a {type(collection)}')
    data.append(new_row)
    
#print(data)