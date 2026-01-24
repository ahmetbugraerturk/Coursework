def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    
    s_ = s
    i=0
    while i < len(s_)-1:
        if i < len(s_)-1 and s_[i]==s_[i+1]:
            s_ = s_[:i] + s_[i+2:]
            i=-1
        i+=1
    return s_