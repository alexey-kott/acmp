from math import sqrt


def main():
    with open('input.txt') as file:
        dots_quantity, q = file.readline().strip().split(" ")
        dots_quantity = int(dots_quantity)
        q = float(q)

        result = "Yes"

        for i in range(dots_quantity):
            x1, y1, x2, y2 = map(int, file.readline().strip().split(" "))

            r1 = sqrt(x1**2+y1**2)
            r2 = sqrt(x2**2+y2**2)
            if r1*q < r2:
                result = "No"

        print(result)


if __name__ == "__main__":
    main()
