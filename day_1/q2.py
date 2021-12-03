from typing import Sequence

import common
import q1


def windowed_sums(container: Sequence[int], window_size: int):
    if len(container) < window_size:
        raise ValueError(
            f"Cannot compute sum; not enough data for window_size={window_size}"
        )
    acc = []
    for i in range(len(container) - window_size + 1):
        acc.append(sum(container[i : i + window_size]))
    return acc


if __name__ == "__main__":
    print(q1.count_increases(windowed_sums(common.depths, 3)))
