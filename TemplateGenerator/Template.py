import os
import regex
import collections
import itertools


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("TestInput.txt", "r") as f:
        lines = f.read().splitlines()


if __name__ == "__main__": main()