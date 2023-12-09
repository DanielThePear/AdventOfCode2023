import os
from functools import reduce
from itertools import takewhile
from sys import maxsize

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(sum(sum((line[-1], reduce(lambda x, y: x + y[-1], reversed([(last_one := [line[i + 1] - line[i] for i in range(len(line) - 1)])] + list(takewhile(lambda x: not all(each == 0 for each in x), ((last_one := [last_one[i + 1] - last_one[i] for i in range(len(last_one) - 1)]) for _ in range(maxsize))))), 0))) for line in tuple(tuple(int(each) for each in line.split()) for line in open("input.txt", "r").read().splitlines())))
