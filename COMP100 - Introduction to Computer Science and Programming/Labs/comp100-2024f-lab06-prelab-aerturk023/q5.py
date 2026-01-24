def longest_consecutive_subsequence_len(list1: list) -> int:
    """
    Finds the length of the longest subsequence of consecutive numbers.

    Parameters:
        list1 (list): The list of integers.

    Returns:
        int: The length of the longest subsequence of consecutive numbers.
    """

    list1.sort()
    curseq = []
    seq = []
    i=0
    while i < len(list1)-1:
        if list1[i]==list1[i+1]:
            list1.pop(i)
            i-=1
        i+=1
    for i in range(1,len(list1)):
        if list1[i-1]==list1[i]-1:
            if curseq != []:
                curseq.pop()
            curseq.append(list1[i-1])
            curseq.append(list1[i])
        else:
            if len(curseq)>len(seq):
                seq = curseq
                curseq = []
        if len(curseq)>len(seq):
            seq = curseq
    return len(seq)

