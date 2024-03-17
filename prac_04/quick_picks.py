import random

MIN_NUM = 1
MAX_NUM = 45
NUM_PER_LINE = 6


def main():
    """Choose sets of random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for a in range(NUM_PER_LINE):
            number = random.randint(MIN_NUM, MAX_NUM)
            while number in quick_pick:
                number = random.randint(MIN_NUM, MAX_NUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
