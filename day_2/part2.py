from collections import Counter

def dist(str1, str2):
    if len(str1) != len(str2):
        raise Exception('Strings must be equal')
    
    return sum([c1 != c2 for c1, c2 in zip(str1, str2)])

def common(str1, str2):
    return ''.join([c1 for c1, c2 in zip(str1, str2) if c1 == c2])

def main():
    codes = []

    with open('input.txt') as f:
        for line in f:
            for other in codes:
                if dist(line, other) == 1:
                    print(common(line, other))
                    return
            codes.append(line)

    codes.sort()

if __name__ == "__main__":
   main()