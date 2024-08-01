from prime_timings import is_prime_factor_fold as p
def find_maxN():
    maxN,maxA, maxB = 0,0,0
    for a in range(-1001, 1000):
        for b in range(-1000, 1001):
            broken = False
            n = 0
            while not broken:
                if p(n**2 + a*n + b):
                    n += 1
                else:
                    broken = True
                    if n-1 > maxN:
                        maxA, maxB, maxN = a, b, n-1
    return maxA * maxB
