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
