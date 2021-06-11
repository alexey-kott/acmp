
def main():
    with open('input.txt') as file:
        file.readline().strip().split(" ")
        prices = list(map(int, file.readline().strip().split(" ")))

    result = 0
    while True:
        if len(prices) == 0:
            break
        value = max(prices)
        index = prices.index(value)
        result += value * (index+1)
        prices = prices[index+1:]

    print(result)


if __name__ == "__main__":
    main()
