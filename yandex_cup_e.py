import sys
from collections import defaultdict


def main():
    n = int(sys.stdin.readline().strip())

    net = defaultdict(dict)

    for i in range(n):
        server1, server2 = map(int, sys.stdin.readline().strip().split())
        net[server1][server2] = 1

    q = int(sys.stdin.readline().strip())
    



if __name__ == "__main__":
    main()
