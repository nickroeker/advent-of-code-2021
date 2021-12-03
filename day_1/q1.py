from typing import Sequence
import operator

import common


def count_increases(nums: Sequence[int]) -> int:
    increases: int = 0

    # Never write hard-to-read code like this,
    # just playing with Python features
    for i in range(len(nums) - 1):
        if operator.lt(*nums[i : i + 2]):
            increases += 1

    return increases


if __name__ == "__main__":
    print(count_increases(common.depths))
