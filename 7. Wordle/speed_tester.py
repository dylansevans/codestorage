import time

def get_feedback(guess, secret):
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

    feedback = [''] * len(guess)
    secret_letter_count = {}
    
    # First pass: handle correct letters (Green)
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = 'G'
        else:
            if secret[i] in secret_letter_count:
                secret_letter_count[secret[i]] += 1
            else:
                secret_letter_count[secret[i]] = 1
    
    # Second pass: handle present but misplaced letters (Yellow)
    for i in range(len(guess)):
        if feedback[i] == '':
            if guess[i] in secret_letter_count and secret_letter_count[guess[i]] > 0:
                feedback[i] = 'Y'
                secret_letter_count[guess[i]] -= 1
            else:
                feedback[i] = "B"


    return ''.join(feedback)

if __name__ == "__main__":
    start = time.perf_counter_ns()
    result = 0b0
    for i in range(1000000):
        result = get_feedback("ABCCE", "EBACZ")
    print((time.perf_counter_ns() - start) // 1000000)
    print(result)
