from string import ascii_lowercase

text = open('input.txt').readline()

min_val = len(text), ''
for ignore in ascii_lowercase:
    result = []
    for c in text:
        if c.lower() == ignore:
            continue
        if not result:
            result.append(c)
            continue
        if abs(ord(c) - ord(result[-1])) == 32:
            result.pop()
        else:
            result.append(c)
    min_val = min(min_val, (len(result), ignore))

print(min_val)
