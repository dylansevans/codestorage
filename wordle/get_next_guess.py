from wordle_game_class import WordleGame

def find_next_word(game):
    best_word = ""
    options_left = game.possible_words
    min_count = 5000

    for guess_option in game.possible_words:
        options_sorter = {}
        for possible_word in options_left:
            code = game.get_guess_results(guess_option, possible_word)
            if code in options_sorter:
                options_sorter[code].append(possible_word)
            else:
                options_sorter[code] = [possible_word]
        
        ### Get maximum guess possibility
        max_count = max([len(x) for x in options_sorter.values()])
        if max_count < min_count:
            min_count = max_count
            best_word = guess_option

    return best_word

def main():
    game = WordleGame()
    guess_results = game.get_guess_results("arise", game.correct_word)
    game.possible_words = game.get_possible_guesses("arise", guess_results)
    if guess_results == "WON":
        return 1
    
    for i in range(2, 7):
        new_guess = find_next_word(game)
        guess_results = game.get_guess_results(new_guess, game.correct_word)
        if guess_results == "WON":
            return i
        game.possible_words = game.get_possible_guesses(new_guess, guess_results)
    return 7

def help():
    game = WordleGame()
    try:
        guess_results = input("What are the results?\n")
    except:
        guess_results = "WON"
        
    game.possible_words = game.get_possible_guesses("arise", guess_results)
    if guess_results == "WON":
        return 1
    
    for i in range(2, 7):
        new_guess = find_next_word(game)
        print(new_guess)
        try:
            guess_results = input("What are the results?\n")
        except:
            guess_results = "WON"
        
        if guess_results == "WON":
            return i
        game.possible_words = game.get_possible_guesses(new_guess, guess_results)



help()
    

def run_many_tests(n):
    total_guesses = 0
    for _ in range(int(n)):
        total_guesses += main()

    print(total_guesses / n)

# run_many_tests(5)