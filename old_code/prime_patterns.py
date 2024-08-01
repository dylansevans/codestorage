import math
from timing_profiler import TimingProfiler

def get_factors(n: int) -> list[int]:
    '''Generates a sorted list of unique integer factors for a given natural number

        Args:
            n (int): The natural number which should be factored

        Returns:
            list: a list of unique integer factors in sorted order

        Examples:
            >>> get_factors(6)
            [1, 2, 3, 6]
            >>> get_factors(17)
            [1, 17]
            >>> get_factors(36)
            [1, 2, 3, 4, 6, 9, 12, 18, 36]
            >>> get_factors(-2)
            []
    '''
    ### BEGIN SOLUTION
    ls = {1,n}
    if n <= 0 or n % 1 != 0:
        return []
    maximum = math.ceil(n ** .5) + 1

    for x in range(2, maximum):
        if n % x == 0:
            ls.add(int(x))
            ls.add(int(n/x))


    return sorted(list(ls))
    ### END SOLUTION

def is_prime(n: int) -> bool:
    '''Determines whether a given integer is prime

       Args:
            n (int): The integer which should be tested

       Returns:
            bool: True if n is prime, False if n is not prime

       Examples:
            >>> is_prime(6)
            False
            >>> is_prime(11)
            True
    '''

    ### BEGIN SOLUTION
    if len(get_factors(n)) == 2:
        return True
    else:
        return False
    ### END SOLUTION 

def largest_prime_factor(n: int) -> int:
    '''Determines the largest prime factor of a given whole number > 1.

       Args:
            n (int): The whole number which should be considered

       Returns:
            int: The largest prime factor of n
                 If the given integer isn't a whole number > 1, returns 0

       Examples:
            >>> largest_prime_factor(6)
            3
            >>> largest_prime_factor(100)
            5
    '''
    ### BEGIN SOLUTION
    if n % 1 != 0 or n <= 0:
        return 0
    found = False
    factors = get_factors(n)
    print(factors)
    greatest = 0
    for i in factors:
        if is_prime(i):
            greatest = i

    return greatest
        
    ### END SOLUTION 

if __name__ == "__main__":
    algorithms = [get_factors, is_prime, largest_prime_factor]
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Verifying Correctness- is_prime
    for algorithm in algorithms:
        actual_primes = []
        for n in range(101):
            if algorithm(n):
                actual_primes.append(n)
        
        if test_primes == actual_primes:
            print(f"{algorithm.__name__} correctly finds primes < 100")
        else:
            print(f"{algorithm.__name__} has a mistake!!")
            print(f"  - Expected: {test_primes}")
            print(f"  - Actual: {actual_primes}")

    # Speed comparisons- is_prime
    inputs = [11, 101, 1009, 10007, 100003, 1000003, 10000019]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    print(experiment.results)
    experiment.graph(title="is_prime Timings", scale="linear")