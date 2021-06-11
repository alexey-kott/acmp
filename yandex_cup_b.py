import sys


def main():
    n, x, k = map(int, sys.stdin.readline().strip().split(" "))
    times = map(int, sys.stdin.readline().strip().split(" "))

    # index = 0
    # times = list(sorted(times))
    # for i in range(min(times), k+1):
    #     for time in times:

    rings = set()
    for time in times:

        time_rings = {time+(x*i) for i in range(0, k+1)}
        rings = rings.union(time_rings)

    for i, ring in enumerate(sorted(rings)):
        if i == k - 1:
            print(ring)


if __name__ == "__main__":
    main()
