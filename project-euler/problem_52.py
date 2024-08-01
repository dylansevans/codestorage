prime_arr = [2,3,5,7,11,13,17,19,23,29]

def prime_hash(num):
    total = 1
    while num > 0:
        digit = num % 10
        num //= 10
        total *= prime_arr[digit]
    return total

def random_handle(num):
    store = prime_hash(num * 2)
    for i in range(3, 7):
        if prime_hash(i * num) != store:
            return False
    return True

found = False
x = 1
while not found:
    if random_handle(x):
        found = True
    else:
        x += 1

print(x)