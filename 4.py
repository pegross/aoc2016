def is_valid_room(name: str, valid_checksum: str) -> bool:
    chars = {}
    for char in list(name):
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    # sort primary by value descending, secondary by key ascending
    sorted_chars = sorted(chars.items(), key=lambda x: (-x[1], x[0]))
    room_checksum = ''

    i = 0
    while i < 5:
        room_checksum += sorted_chars[i][0]
        i += 1

    return room_checksum == valid_checksum


def decrypt_shift_cipher(name: str, steps: int, alphabet: list) -> str:
    decrypted = ''
    for char in list(name):
        try:
            index = (alphabet.index(char) + steps) % 26
            decrypted += alphabet[index]
        except ValueError:
            print(char, steps, steps % 26)

    return decrypted


lines = []
with open('input/4') as f:
    for line in f:
        lines.append(line.strip())

room_sum = 0;
for line in lines:
    parts = line.split('-')
    num_checksum = parts[-1].split('[')
    room_name = ''.join(parts[:-1])
    room_number = int(num_checksum[0])

    # part b - decrypt room name shift cipher
    room_name = decrypt_shift_cipher(room_name, room_number, list('abcdefghijklmnopqrstuvwxyz'))
    if room_name == 'northpoleobjectstorage':
        print(room_number)

    # part a - validate room names
    if is_valid_room(room_name, num_checksum[1].strip(']')):
        room_sum += room_number

# print(room_sum)
