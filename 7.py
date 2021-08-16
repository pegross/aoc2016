import re


def has_abba(sequence: str) -> bool:
    seq_len = len(sequence)
    i = 0
    while i + 3 < seq_len:
        if sequence[i] == sequence[i + 3] and sequence[i + 1] == sequence[i + 2] and not sequence[i] == sequence[i + 1]:
            return True
        i += 1

    return False


def sequences_have_abba(sequences: list) -> bool:
    for seq in sequences:
        if has_abba(seq):
            return True
    return False


amount = 0
pattern = '\[.*?]'

with open('input/7') as f:
    for line in f:
        hypernet_sequences = re.findall(pattern, line)
        line = re.sub(pattern, '|', line)
        supernet_sequences = line.split('|')

        if not sequences_have_abba(hypernet_sequences) and sequences_have_abba(supernet_sequences):
            amount += 1

print(amount)
