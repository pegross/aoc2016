from enum import IntEnum
from collections import deque
from typing import Tuple


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def apply_instructions(pos: Tuple[int, int, Direction], instructions: deque, visited: dict = {}) \
        -> Tuple[int, int, Direction]:
    if not instructions:
        return pos

    instruction = instructions.popleft()
    origin_x = x = pos[0]
    origin_y = y = pos[1]

    # determine which direction we are facing
    dir_mod = 1 if instruction[0] == 'R' else -1
    new_dir = Direction((pos[2] + dir_mod) % len(Direction))
    steps = int(instruction[1:])

    if new_dir == Direction.NORTH:
        y += steps

    if new_dir == Direction.SOUTH:
        y -= steps

    if new_dir == Direction.EAST:
        x += steps

    if new_dir == Direction.WEST:
        x -= steps

    # part 2 shenanigans
    hit = check_visited(origin_x, origin_y, x, y, visited)
    if hit:
        return hit[0], hit[1], new_dir

    return apply_instructions((x, y, new_dir), instructions, visited)


def check_visited(x, y, target_x, target_y, visited: {}):
    key = str(x) + "/" + str(y)
    if key in visited:
        return x, y

    # we actually moved - mark position
    if x != target_x or y != target_y:
        visited[key] = 1

    if x < target_x:
        return check_visited(x + 1, y, target_x, target_y, visited)
    if x > target_x:
        return check_visited(x - 1, y, target_x, target_y, visited)
    if y < target_y:
        return check_visited(x, y + 1, target_x, target_y, visited)
    if y > target_y:
        return check_visited(x, y - 1, target_x, target_y, visited)


instruction_list = []
with open('input/1') as f:
    for line in f:
        instruction_list.extend(list(map(lambda x: x.strip(), line.split(','))))

instruction_queue = deque(instruction_list)
final_pos = apply_instructions((0, 0, Direction.NORTH), instruction_queue)

print(abs(final_pos[0]) + abs(final_pos[1]))
