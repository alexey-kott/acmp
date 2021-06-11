def check_coord(cell: str) -> None:
    if len(cell) != 2:
        raise ValueError('error')
    if ord(cell[0]) < 65 or ord(cell[0]) > 72:
        raise ValueError('error')
    if int(cell[1]) > 8 or int(cell[1]) < 1:
        raise ValueError('error')


def check_move(cell1: str, cell2: str) -> bool:
    diff1 = ord(cell1[0]) - ord(cell2[0])
    diff2 = ord(cell1[1]) - ord(cell2[1])

    if diff1 * diff2 in [2, -2]:
        return True
    return False


def main():
    with open("input.txt") as file:
        try:
            cell1, cell2 = file.readline().strip().split("-")
            check_coord(cell1)
            check_coord(cell2)
        except ValueError:
            print('ERROR')
            return

        result = check_move(cell1, cell2)
        if result:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
