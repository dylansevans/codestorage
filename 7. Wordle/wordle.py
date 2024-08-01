from valid_wordle_guesses import get_valid_wordle_guesses
from wordle_secret_words import get_secret_words

def get_feedback(guess: str, secret_word: str) -> str:
    ### BEGIN SOLUTION
    guess = guess.upper()
    secret_word = secret_word.upper()
    letters_left = list(guess)
    secret_letters = list(secret_word.upper())
    answer = ["-"] * 5
    for index, letter in enumerate(guess):
        if letter == secret_word[index]:
            answer[index] = letter.upper()
            letters_left[index] = ""
            secret_letters.remove(letter)
    for index, letter in enumerate(letters_left):
        if letter in secret_letters:
            answer[index] = letter.lower()
            secret_letters.remove(letter)

    return "".join(answer)

    ### END SOLUTION 

def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
        
        Args:
         guesses (list): A list of string guesses, which could be empty
         feedback (list): A list of feedback strings, which could be empty
         secret_words (set): A set of potential secret words
         valid_guesses (set): A set of valid AI guesses
        
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    ### BEGIN SOLUTION
    ai = AI(secret_words, valid_guesses)
    for index, guess in enumerate(guesses):
        ai.possible_secret_words = ai.narrow_down(feedback[index], guess)

    return ai.get_next_guess(len(guesses) + 1)
    ### END SOLUTION 
    

class AI:
    def __init__(self, secret_word_list, valid_guesses):
        self.possible_guesses = valid_guesses
        self.possible_secret_words = secret_word_list
    
    def get_next_guess(self, guess_number):
        min_guess = 5000
        best_guess = ""

        if guess_number == 1:
            return "SALET"

        for guess in self.possible_secret_words:
            guess_dict = {}

            for secret_word in self.possible_secret_words:
                result = self.get_feedback(guess, secret_word)
                guess_dict[result] = guess_dict.get(result, 0) + 1

            max_guess = max(guess_dict.values())
            if max_guess < min_guess:
                min_guess = max_guess
                best_guess = guess

        return best_guess

    def narrow_down(self, result, guess):
        possible = set()
        # Narrow down possible_secret_words and possible_guesses
        for secret_word in self.possible_secret_words:
            if get_feedback(guess, secret_word) == result:
                possible.add(secret_word)

        #TODO narrow down possible guesses?

        return possible
    
    def get_feedback(self, guess, secret):
        secret_list = set(secret)
        bit = 0b0000000000
        
        # First pass: handle correct letters (Green)
        for i in range(5):
            if guess[i] == secret[i]:
                bit |= 1 << i + 5
            else:
                if guess[i] in secret_list:
                    bit |= 1 << i
        

        return bit
    

if __name__ == "__main__":
    print(get_AI_guess(["SLATE", "DRANK"],["--A--", "-RAn-"], get_secret_words(), get_valid_wordle_guesses()))