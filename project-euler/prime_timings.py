import math

def is_prime_factor_fold(n: int) -> bool:
    if n <= 1:
        return False
    max = math.ceil(math.sqrt(n)) + 1
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for x in range(3, max, 2):
        if n % x == 0:
            return False
        
    return True