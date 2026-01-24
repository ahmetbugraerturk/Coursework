def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    def make_int(a):
        a = a[2:]
        intV = 0
        for i in range(len(a)):
            intV += int(a[-i-1])*(2**i)
        return intV
    
    def make_bin(intV):
        s = ""
        while intV!=0:
            s = str(intV%2)+s
            intV = intV//2
        return "0b"+s

    sumInt = make_int(a)+make_int(b)
    sumBin = make_bin(sumInt)
    
    return sumBin