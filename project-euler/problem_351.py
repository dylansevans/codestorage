from prime_timings import is_prime_factor_fold as p

def get_all_primes(n):
    #returns list of primes at O(n/2) efficiency
    list_of_primes = [1]

    while n % 2 == 0:
        list_of_primes.append(2)
        n /= 2
    
    x = 3
    while x <= n:
        while n % x == 0:
            list_of_primes.append(x)
            n /= x
        x += 2
    
    return len(list_of_primes)


def main(n):
    summation = 0
    for i in range(2, n + 1):
        summation += get_all_primes(i) - 1
    return summation * 6

print(main(1000))
