import hashlib

input = 'reyedfim'
pw_list = {}

i = 0
while len(pw_list) < 8:
    full_input = input + str(i)
    hex = hashlib.md5(full_input.encode('utf-8')).hexdigest()
    print(full_input, hex)

    if hex[:5] == '00000':
        try:
            key = int(hex[5])
            if key <= 7 and key not in pw_list:
                pw_list[key] = hex[6]
        except ValueError:
            print(hex[5])
    i += 1


password = ''
for k, v in sorted(pw_list.items()):
    password += str(v)

print(password)