sum_value = 0

for i in range(1000000):
    stringed = str(i)
    string_binary = '{0:08b}'.format(i).lstrip("0")

    if stringed == stringed[::-1].lstrip("0") and string_binary.lstrip("0") == string_binary[::-1].lstrip("0"):
        sum_value += i

print(sum_value)