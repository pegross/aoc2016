import numpy as np


def rect(_screen: np.ndarray, width: int, height: int):
    _screen[0:height, 0:width] = 1
    return _screen


def rotate(_screen, axis: str, start: int, by: int):
    # shift column down
    if axis == 'x':
        _screen[:, start] = np.roll(_screen[:, start], by, 0)

    # shift row right
    if axis == 'y':
        _screen[start, :] = np.roll(_screen[start, :], by, 0)

    return _screen


screenHeight = 6
screenWidth = 50
screen = np.zeros((screenHeight, screenWidth))

with open('input/8') as f:
    i = 0
    for line in f:
        print('screen', i + 1, screen)
        tokens = line.rstrip().split(' ')
        if tokens[0] == 'rect':
            size = tokens[1].split('x')
            screen = rect(screen, int(size[0]), int(size[1]))

        if tokens[0] == 'rotate':
            start = tokens[2].split('=')[1]
            screen = rotate(screen, tokens[2][0], int(start), int(tokens[4]))

        i += 1
        if i > 15:
            exit()
    print(np.count_nonzero(screen == 0))
