signals = []
with open('input/6') as f:
    # prepare signals array
    i = 0
    lineLen = len(f.readline().strip())
    while i < lineLen:
        signals.append([])
        i += 1

    # read chars to correct signals index
    f.seek(0)
    for line in f:
        chars = enumerate(line.strip())
        for k, v in chars:
            signals[k].append(v)

# part a: max repetitions
msg_max = ''
# part b: min repetitions
msg_min = ''

for signal in signals:
    msg_max += max(signal, key=signal.count)
    msg_min += min(signal, key=signal.count)

print('max: ', msg_max)
print('min: ', msg_min)
