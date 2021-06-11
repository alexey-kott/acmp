def main():
    sequence = [1, 4, 7, 3, 2, 8, 15]

    min_n = min(sequence)
    max_n = max(sequence)

    sections = []
    section = []
    for i in range(min_n, max_n+1):
        if i in sequence:
            section.append(i)
        elif len(section) != 0:
            sections.append(section)
            section = []

        if i == max_n:
            sections.append(section)

    print(sections)


if __name__ == "__main__":
    main()
