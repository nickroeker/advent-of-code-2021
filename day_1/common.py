import aocd

__puzzle = aocd.models.Puzzle(year=2021, day=1)
depths: list[int] = [int(line) for line in __puzzle.input_data.splitlines()]
