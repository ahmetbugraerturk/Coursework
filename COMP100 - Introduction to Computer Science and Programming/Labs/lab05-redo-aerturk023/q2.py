def longest_common_prefix(strs):
    """
    Write a Python function longest_common_prefix(strs) that takes a string containing three strings seperated by whitespace
    and returns the longest common prefix among all the strings in the list. 
    If there is no common prefix, return an empty string.
    """
    str1, str2, str3 = strs.split()
    i=0
    result = ""
    while str1[i] == str2[i] == str3[i]:
        result += str1[i]
        i += 1
    return result
    





