def check_rotation(s1,s2):
    """
    Given two strings s1 and s2, determine if one string is a rotation of the other.

    """
    if len(s1) != len(s2):
        return False
    
    for s in range(len(s1)):
        if s1[s:] + s1[:s] == s2:
            return True;
    return False
    pass

