prev1 = 0
prev2 = 1
sum = 0

while True:
    prev1 += prev2
    if prev1 > 4000000:
        break
    if prev1 % 2 == 0:
        sum += prev1
    prev2 += prev1
    if prev2 > 4000000:
        break
    if prev2 % 2 == 0:
        sum += prev2

print(sum)