import re


# part a
def get_abba(sequence: str) -> bool:
    seq_len = len(sequence)
    i = 0
    while i + 3 < seq_len:
        if sequence[i] == sequence[i + 3] and sequence[i + 1] == sequence[i + 2] and not sequence[i] == sequence[i + 1]:
            return True
        i += 1
    return False


def sequences_have_abba(sequences: list) -> bool:
    for seq in sequences:
        if get_abba(seq):
            return True
    return False


# part b
def get_aba(sequence: str, aba: list = []) -> list:
    seq_len = len(sequence)
    i = 0
    while i + 2 < seq_len:
        if sequence[i] == sequence[i + 2] and not sequence[i] == sequence[i + 1]:
            if not aba or sequence[i] == aba[1] and sequence[i + 1] == aba[0]:
                # first char, second char, index to split at
                return [sequence[i], sequence[i + 1], i + 1]
        i += 1
    return []


def sequences_support_ssl(supernet: list, hypernet: list) -> bool:
    for sup_seq in supernet:
        while match := get_aba(sup_seq):
            print(sup_seq)
            for hyp_seq in hypernet:
                if get_aba(hyp_seq, match):
                    return True
            sup_seq = sup_seq[match[2]:]
    return False


amount = 0
pattern = '\[.*?]'

with open('input/7') as f:
    for line in f:
        hypernet_sequences = re.findall(pattern, line)
        line = re.sub(pattern, '|', line)
        supernet_sequences = line.split('|')

        if sequences_support_ssl(supernet_sequences, hypernet_sequences):
            amount += 1

print(amount)
