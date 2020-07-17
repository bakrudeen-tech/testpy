import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mark1", help="mark1")
    parser.add_argument("--mark2", help="mark2")
    parser.add_argument("--operation", help="operation")

    args = parser.parse_args()

    m1 = int(args.mark1)
    m2 = int(args.mark2)
    if args.operation == 'add':
        result = m1+m2
        print(result)