from patternmatch import pattern_match
from revcompliment import rev_comp

txt = input("Filename: ")
pattern = input("Pattern: ")

print(pattern)
positions, count = pattern_match(txt, pattern)
for position in positions:
        print(position, end=' ')
print()
print(count)

print(rev_comp(pattern))
positions2, count2 = pattern_match(txt, rev_comp(pattern))
for position in positions2:
        print(position, end=' ')
print()
print(count2)

print("Total: ", count + count2)