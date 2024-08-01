import math

total = 1000000

def main(total_cubes):
    count = 0

    max_half_width = math.ceil(total_cubes / 4)

    for i in range(1, max_half_width + 2):
        for x in range(i - 2, 0, -2):
            if i * i - x * x <= total:
                count += 1

    return count

print(main(total))

successes = []

with open("./passcodes.txt", "r") as f:
    for line in f:
        successes.append(line.strip())



def check_passcode(code):
    code = str(code)
    code_length = len(code)
    for success in successes:
        index = 0
        for letter in success:
            while letter != code[index]:
                if code_length == index + 1:
                    return False
                index += 1
            if not code_length == index + 1:
                index += 1

    return True


def try_all():
    passcode = 10
    while not check_passcode(passcode):
        passcode += 1
    
    print(passcode)

try_all()
