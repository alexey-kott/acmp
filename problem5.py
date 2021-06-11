

def main():
    with open("input.txt") as file:
        file.readline()
        marks = map(int, file.readline().strip().split(" "))

        stat = {"3": [],
                "4": []}
        for mark in marks:
            if mark % 2 == 0:
                stat["4"].append(mark)
            else:
                stat["3"].append(mark)

        print(" ".join(map(str, stat["3"])))
        print(" ".join(map(str, stat["4"])))

        if len(stat["3"]) > len(stat["4"]):
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()
