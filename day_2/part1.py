from collections import Counter

def main():
    three_count = 0
    two_count = 0

    with open('input.txt') as f:
        for line in f:
            char_count = Counter(line)
            if 3 in char_count.values():
                three_count += 1
            if 2 in char_count.values():
                two_count += 1

    checksum = three_count*two_count
    print('Three count: {}\nTwo count: {}'.format(three_count, two_count))
    print('Checksum: {}'.format(checksum))

if __name__ == "__main__":
   main()