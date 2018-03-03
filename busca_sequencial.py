def busca( seq, x):
    '''(list, float) -> bool'''
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return False