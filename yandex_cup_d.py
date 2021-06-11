import sys


def main():
    n = int(sys.stdin.readline().strip())

    if n == 1:
        print(f"! 1", flush=True)
        return

    commits = {}

    check_commit = n // 2
    last_good = 0
    first_bad = n + 1
    while True:
        print(check_commit, flush=True)
        result = int(sys.stdin.readline().strip())
        commits[check_commit] = result
        if result:
            if check_commit > last_good:
                last_good = check_commit
        else:
            if check_commit < first_bad:
                first_bad = check_commit

        if first_bad - 1 == last_good:
            print(f"! {first_bad}", flush=True)
            break

        check_commit = (first_bad + last_good) // 2


if __name__ == "__main__":
    main()
