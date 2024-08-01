def get_words():
    words_set = []
    with open("official_words.txt", "r") as f:
        words_set = [x.strip() for x in f.readlines()]
    return words_set