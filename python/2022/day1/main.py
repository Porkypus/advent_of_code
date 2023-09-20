import os
import sys

print(
    sum(
        sorted(
            [
                sum([int(i) for i in x.split("\n")])
                for x in open(os.path.join(sys.path[0], "input.txt"))
                .read()
                .split("\n\n")
            ]
        )[-3:]
    )
)
