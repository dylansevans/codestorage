from get_all_words import get_words
import random

class WordleGame:
    def __init__(self):
        self.possible_words = get_words()
        self.correct_word = random.choice(self.possible_words)

    def get_possible_guesses(self, guess, guess_results):
        new_correct_words = set()

        for check_word in self.possible_words:
            if self.get_guess_results(guess, check_word) == guess_results:
                new_correct_words.add(check_word)
            
        return new_correct_words

    def get_guess_results(self, guess, correct = "basic"):
        guess_list = list(guess)
        letters_left = list(correct)
        results = 0

        #check for correct positions
        for i, let in enumerate(guess_list):
            if let == correct[i]:
                results += 2 * (10**(4-i))
                letters_left.remove(let)
                guess_list[i] = ""
        
        if len(letters_left) == 0:
            return "WON"

        #check for incorrect positions
        for i, let in enumerate(guess_list):
            if let != "":
                if let in letters_left:
                    results += 10**(4-i)
                    letters_left.remove(let)
        
        return results