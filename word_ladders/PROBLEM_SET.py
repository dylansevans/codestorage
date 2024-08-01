from valid_ladders_word_list import get_valid_word_list

count = 0

word_list = get_valid_word_list()
length = len(word_list)



def valid(word):
    for w2 in word_list:
        if len(word) == len(w2) and w2 != word:
            for x in range(len(word)):
                if word[x] == w2[x]:
                    return False
    return True

print(valid("aloof"))


length = len(word_list)

for i in range(length):
    if valid(word_list[i]): count += 1

print(count)