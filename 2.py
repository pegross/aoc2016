class Numpad:
    sequence = ""
    numbers = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def up(self):
        self.y = max(self.y - 1, 0)

    def down(self):
        self.y = min(self.y + 1, 2)

    def left(self):
        self.x = max(self.x - 1, 0)

    def right(self):
        self.x = min(self.x + 1, 2)

    def press(self):
        print(self.x, self.y, self.numbers[self.y][self.x])

        self.sequence += str(self.numbers[self.y][self.x])

    def get_sequence(self) -> str:
        return self.sequence


instructions = []
with open('input/2') as f:
    for line in f:
        instructions.append(list(line))

numpad = Numpad()
for sequence in instructions:
    for token in sequence:
        if token == 'U':
            numpad.up()
        if token == 'L':
            numpad.left()
        if token == 'D':
            numpad.down()
        if token == 'R':
            numpad.right()
    numpad.press()

print(numpad.get_sequence())
