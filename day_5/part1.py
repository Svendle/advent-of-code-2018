text = open('input.txt').readline()

output = []
for c in text:
    if not output:
        output.append(c)
        continue
    if abs(ord(c) - ord(output[-1])) == 32:
        output.pop()
    else:
        output.append(c)
    
print(len(text))
print(len(output))