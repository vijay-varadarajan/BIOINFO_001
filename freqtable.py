def freq_table(txt, k):
    freqmap = {}
    for i in range(len(txt) - k):
        cur_seq = ''
        for j in range(i, k):
            cur_seq += txt[j]

        added = False
        for elem in freqmap:
            if elem['name'] == cur_seq:
                elem['count'] += 1
                added = True
        
        