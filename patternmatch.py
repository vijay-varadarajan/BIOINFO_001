def main():
    txt = input("Filename: ")
    pattern = input("Pattern: ")
    print(pattern_match(txt, pattern))


# Checks for presence of given pattern in txt
# Returns the indexes in which the pattern begins and the total number of occurences
def pattern_match(txt, pattern):
    with open(txt, 'r') as file:
            txt = file.read()
            
    positions = []
    for i in range(len(txt) - len(pattern) + 1):
            cur_seq = txt[i:i+len(pattern)]

            if cur_seq.upper() == pattern.upper():
                    positions.append(i)

    return positions, len(positions)


if __name__ == "__main__":
    main()