import os
import sys

symbols = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}

wins = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER",
}

print(
    sum(
        [
            (symbols[symbols[y[1]]] + 6)
            if wins[symbols[y[1]]] == symbols[y[0]]
            else (
                symbols[symbols[y[1]]] + 3
                if symbols[y[0]] == symbols[y[1]]
                else symbols[symbols[y[1]]]
            )
            for y in [
                x.split(" ")
                for x in open(os.path.join(sys.path[0], "input.txt")).read().split("\n")
            ]
        ]
    )
)
