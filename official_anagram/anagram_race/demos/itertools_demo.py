from itertools import combinations, permutations

letters = list("Academy")

print("\nPermutation: Arrangement of elements in a specific order")
print("As the number of letters in a word increase, the number of permutations of the letters in the word grow at a factorial rate:")
for i in range(1, len(letters)+1):
  word = letters[0:i]
  perms = list(permutations(word))
  print(f"{word} has {len(word)} letters and {len(perms)} letter permutations.")

print("\nCombination: Number of objects selected from a group ")
num = 3
combos = list(combinations(letters, num))
print(f"There are {len(combos)} ways to choose {num} letters from {letters}:")
print(combos)
