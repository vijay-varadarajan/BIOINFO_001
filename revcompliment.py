def main():
    text = input("Text: ")
    print(rev_comp(text))

# Returns the reverse complement of a particular strand of DNA
def rev_comp(pattern):
    rc = ''
    for base in pattern.upper():
        if base == 'A':
            rc += 'T'
        if base == 'T':
            rc += 'A'
        if base == 'C':
            rc += 'G'
        if base == 'G':
            rc += 'C'
    
    return rc[::-1]

if __name__ == "__main__":
    main()