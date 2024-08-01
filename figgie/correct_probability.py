import random
import matplotlib.pyplot as plt

def round():
    cards = [False] * 40

    for i in range(12):
        rand = random.randint(0,39)

        while cards[rand]:
            rand = random.randint(0,39)

        cards[rand] = True

    count_of_main = 0

    for card in cards[:10]:
        if card:
            count_of_main += 1

    return count_of_main

if __name__ == "__main__":
    games = [0] * 11
    rounds = 10000

    for i in range(rounds):
        games[round()] += 1

    adjusted = [x / rounds for x in games]

    plt.bar(range(0,11), adjusted, color = "skyblue", edgecolor = "black")

    plt.xlabel("Number of Highest Frequency")
    plt.ylabel("Frequency")
    plt.title("Figgie Starting Hand Distribution")

    plt.show()