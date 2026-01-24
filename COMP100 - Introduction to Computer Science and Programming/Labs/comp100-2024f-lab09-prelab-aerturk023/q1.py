def generate_all_strings(letter_sequence):
    """
    Generate all possible strings by removing letters from the input string 
    while maintaining the original order.
    
    Args:
    letter_sequence (str): Input string with no duplicate letters
    
    Returns:
    list: A sorted list of all possible strings (in descending order of length)
    """
    subset = []
    
    def gen_str(s, subset):
        if s not in subset:
            subset.append(s)
        for i in range(len(s)):
            gen_str(s[:i]+s[i+1:], subset)
            
    gen_str(letter_sequence, subset)
    
    return sorted(sorted(subset), key=lambda x: len(x), reverse=True)