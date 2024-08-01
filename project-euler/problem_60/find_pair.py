import pickle
from itertools import permutations
primes = []

with open("./primes.txt", "rb") as f:
    primes = pickle.load(f)

primes = [str(x) for x in primes]
primes_set = set(primes)

length = len(primes)

def check_values(x1, x2, x3, x4, x5):
    #TODO check all concatenations
    all_combos = permutations([x1, x2, x3, x4, x5], 2)
    for combo in all_combos:
        if combo[0] + combo[1] not in primes_set:
            return False
    return True



def main():
    for x1 in range(200):
        for x2 in range(x1, 200):
            for x3 in range(x2, 200):
                for x4 in range(x3, 200):
                    for x5 in range(x4, 200):
                        if check_values(primes[x1],primes[x2],primes[x3],primes[x4],primes[x5]): return primes[x1]+primes[x2]+primes[x3]+primes[x4]+primes[x5]


print(main())