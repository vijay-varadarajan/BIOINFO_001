# Code Challenge: Implement PatternCount (reproduced below).
# Input: Strings Text and Pattern.
# Output: Count(Text, Pattern).

def main():
    print(PatternCount(input("text: "), input("Pattern: ")))

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i: len(pattern)+i] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    main()