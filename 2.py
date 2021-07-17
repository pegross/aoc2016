class Numpad:
    sequence = ""
    numbers = (
        ('-', '-', '1', '-', '-'),
        ('-', '2', '3', '4', '-'),
        ('5', '6', '7', '8', '9'),
        ('-', 'A', 'B', 'C', '-'),
        ('-', '-', 'D', '-', '-')
    )

    def __init__(self, x: int = 1, y: int = 1):
        self.x = x
        self.y = y

    def up(self):
        self.move(self.x, self.y - 1)

    def down(self):
        self.move(self.x, self.y + 1)

    def left(self):
        self.move(self.x - 1, self.y)

    def right(self):
        self.move(self.x + 1, self.y)

    def move(self, x: int, y: int):
        if y < 0 or x < 0:
            return
        if y >= len(self.numbers) or x >= len(self.numbers[y]) or self.numbers[y][x] == '-':
            return
        self.x = x
        self.y = y

    def press(self):
        print(self.x, self.y, self.numbers[self.y][self.x])
        self.sequence += str(self.numbers[self.y][self.x])

    def read(self) -> str:
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

print(numpad.read())
