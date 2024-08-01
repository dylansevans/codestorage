import random
import matplotlib.pyplot as plt

all_totals = [0] * 11
for x in range(11):
    all_totals[x] = []


def round():
    cards = [5] * 40
    all_choices = list(range(0,40))
    for index, x in enumerate([12,10,10,8]):
        for i in range(x):
            rand = random.choice(all_choices)
            all_choices.remove(rand)
            cards[rand] = index
    
    for i in range(0,4):
        count = 0
        for card in cards[:10]:
            if card == i:
                count += 1

        all_totals[count].append(i == 0)

def get_probability(array):
    for index, value in enumerate(array):
        total = 0
        common_suit_count = 0
        for x in value:
            if x:
                common_suit_count += 1
            total += 1
        try:
            all_totals[index] = common_suit_count / total
        except ZeroDivisionError:
            all_totals[index] = 0
    return array


if __name__ == "__main__":
    rounds = 5000000

    for i in range(rounds):
        round()

    new_array = get_probability(all_totals)

    # Add value labels

    plt.bar(range(0,11), all_totals, color = "skyblue", edgecolor = "black")

    # for i, h in enumerate(new_array):
    #     plt.text(new_array[i], h, str(h), ha='center', va='bottom')

    plt.xlabel("Number of Highest Frequency")
    plt.ylabel("Frequency")
    plt.title("Figgie Starting Hand Distribution")

    plt.show()
