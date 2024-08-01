import math
import pickle

def is_prime_factor_fold(n: int) -> bool:
    '''Determines whether a given integer is prime
    '''
    if n <= 1:
        return False
    ### BEGIN SOLUTION
    max = math.ceil(math.sqrt(n)) + 1
    if n % 2 == 0:
        return False
    
    for x in range(3, max, 2):
        if n % x == 0:
            return False
        
    return True
    ### END SOLUTION

primes = [2,3,5,7,11]

for x in range(13, 10000000, 2):
    if is_prime_factor_fold(x): primes.append(x)


with open("./primes.txt", "wb") as f:
    pickle.dump(primes, f)