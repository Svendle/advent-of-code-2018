
def find_dup():
    freq = 0
    freqs = {0}
    while True:
        with open('input.txt') as f:
            for line in f:
                freq += int(line)
                if freq in freqs:
                    return freq
                freqs.add(freq)

if __name__ == "__main__":
    print(find_dup())