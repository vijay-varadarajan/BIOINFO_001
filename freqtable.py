from tabulate import tabulate

def main():
    freqtable = (freq_table(input("Filename: "), int(input("k: "))))
    print(tabulate(freqtable, headers='keys', tablefmt='pretty'))
    
    with open('freqtable_V_cholerae.txt', 'w') as file:
        file.write(str(freq_table))

# Takes as input filename and k value
# Gives a list of dictionaries containing the k mer with maximum repeats 
def freq_table(name, k):
    with open(name, 'r') as file:
        txt = file.read()

    freqdict = []
    for s in range(k, k+1):
        elements = {}
        for i in range(len(txt) - k):
            cur_seq = txt[i : s+i]
            
            if not elements:
                elements[cur_seq] = 1
                continue
            
            added = False
            for seq, count in elements.items():
                if cur_seq == seq:
                    count += 1
                    elements.update({cur_seq : count})
                    added = True
            
            if not added:
                elements[cur_seq] = 1

        max_element = {list(elements)[0] : list(elements.values())[0]}
        max_value = 0
        seq_with_max_kmers = []

        for element in elements:
            if elements[element] >= dict(max_element)[list(max_element)[0]]:
                max_element = {element : elements[element]}
                max_value = elements[element]

        for element in elements:
            if elements[element] == max_value:      
                seq_with_max_kmers.append({'k':s, 'count':elements[element], f'{s}-mers':element})
        
        freqdict += seq_with_max_kmers

    return freqdict

        
if  __name__ == "__main__":
    main()