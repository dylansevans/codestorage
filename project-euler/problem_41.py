from prime_timings import is_prime_factor_fold as p

def main():
    for i in range(7777777, 1, -2):
        if ''.join(sorted(list(set(str(i))))) == ''.join(sorted(list(str(i)))):
            if not ("0" in list(str(i)) or "9" in list(str(i)) or "8" in list(str(i))):
                if p(i):
                    print(i)
                    return i
                
main()