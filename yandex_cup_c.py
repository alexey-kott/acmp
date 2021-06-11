import sys


def main():
    points, card_quantity = map(int, sys.stdin.readline().strip().split(" "))

    cards = list(map(int, sys.stdin.readline().strip().split(" ")))

    petya = 0
    vasya = 0

    for card in cards:
        if card % 3 == 0 and card % 5 == 0:
            continue
        if card % 3 != 0 and card % 5 != 0:
            continue

        if card % 3 == 0:
            petya += 1
        if card % 5 == 0:
            vasya += 1

        if petya == points:
            print("Petya")
            return
        if vasya == points:
            print("Vasya")
            return

    if petya > vasya:
        print("Petya")
    elif petya < vasya:
        print("Vasya")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
