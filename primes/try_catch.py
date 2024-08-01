try:
    n = {}
    n["a"] += 1
except ZeroDivisionError:
    print("What the sigma")
except KeyError:
    n["a"] = 0

print(n)