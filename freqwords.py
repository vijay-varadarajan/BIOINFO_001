import sys

def main():
    txt = input("Filename: ")
    k = int(input("k: "))

            
    # opens file of name given in cmd line argument
    with open(txt, 'r') as file:
        line = file.read()
    
    '''
    print()
    for dic in output:
        print(f"{dic['pattern']} : {dic['count']}\n")
    '''

    # Computes the counts of each pattern and the pattern with maximum count
    # Store the pattern with maximum count in a file 
    counts, output = freq_words(k, str(line))
    with open("output.txt", 'w') as file:
        for seq in output:
            file.write("MAX: " + str(seq) + "\n")
        file.write("\n3 or more repeats: \n")

    # Stores all patterns with 3 or more repeats in a file
    for count in counts:
        if count['count'] >= 3:
            print(count)
            with open("output.txt", 'a') as file:
                file.write(str(count) + "\n")


def freq_words(k, txt):
    counts = []

    for i in range(len(txt) - k + 1):
        cur_seq = ''
        for j in range(i, k + i):
            cur_seq += txt[j]
    
        added = False
        for elem in counts:
            if elem['pattern'] == cur_seq:
                elem['count'] += 1
                added = True
    
        if not added:
            counts.append({'pattern': cur_seq, 'count' : 1, 'position' : i+1})

    
    max_count = counts[0]['count']
    output = []
    for i in counts:
        if i['count'] > max_count:
            max_count = i['count']
            output = [i]
        elif i['count'] == max_count:
            output.append(i)
        else:
            continue

    return counts, output

main()