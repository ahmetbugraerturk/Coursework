def longest_palindromic_substring(s):
    '''
    Given a string find the longest palindromic substring
    '''
    lps = ""
    final_lps= ""
    for i in range(len(s)):
        if i < len(s)-1 and s[i]==s[i+1]:
            j=0
            while i < len(s)-1-j and s[i-j]==s[i+1+j]:
                lps = s[i-j:i+2+j]
                j+=1
        elif i<len(s)-2 and s[i]==s[i+2]:
            j=0
            while i < len(s)-2-j and s[i-j]==s[i+2+j]:
                lps = s[i-j:i+3+j]
                j+=1
        if len(lps)>len(final_lps):
            final_lps=lps
                
    return final_lps