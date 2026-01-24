def first_non_repeating_character(s):
    """
    Given a string s, find the first character that doesn’t repeat in the string and return its index.
     If every character in the string repeats, return -1.

    """
    # Delete the pass and code
    i = 0
    while i < len(s):
        if s[i] != s[i+1]:
            return i
        else:
            i += 1
        i += 1
    return -1

print(first_non_repeating_character("aabbcd"))


print(first_non_repeating_character("ccoommpp"))

print(first_non_repeating_character("python"))



