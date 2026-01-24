def compress_string(s):
    """
    Write a function `compress_string(s)` that takes a string `s` as input 
    and returns a compressed version of the string. 
    The compressed string should replace consecutive duplicates of a character with the character 
    and the count of the consecutive duplicates. If the compressed string is not smaller than the original string, return the original string.

    """
    n = len(s)
    i = 0
    ans = ""
    while i < n:
        j = i
        while j < n and s[i] == s[j]:
            j += 1
        ans += s[i] + str(j - i)
        i = j
    if len(ans) < n:
        return ans
    return s
