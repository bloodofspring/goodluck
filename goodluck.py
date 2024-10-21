import argparse

from goodluck import GoodLuck


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chance', help="Шанс на выигрыш", default=0.5, type=float)
    parser.add_argument('-t', '--time', help="Время загрузки", default=5.0, type=float)

    args = parser.parse_args()
    GoodLuck(chance=args.chance, load_time=args.time).try_()


if __name__ == "__main__":
    main()
