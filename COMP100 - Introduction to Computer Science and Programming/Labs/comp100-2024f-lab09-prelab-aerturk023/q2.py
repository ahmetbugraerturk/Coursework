def simulate(letter_sequence):
    """
    Simulate letter crushing by removing consecutive identical letters from left.
    
    Args:
    letter_sequence (str): Input string to simulate crushing
    
    Returns:
    str: Resulting sequence after crushing or 'Literal Crush!' if all letters disappear
    """
    def crush(s):
        d = ""
        count = 1
        for i in range(len(s)):
            if i+1 < len(s) and s[i] == s[i+1]:
                d=s[i]
                count += 1
            else:
                if d != "":
                    return crush(s[:i-count+1]+s[i+1:])
        return s
    cr = crush(letter_sequence)
    if cr == "":
        return "Literal Crush!"
    else:
        return cr