def count_files(directory):
    
    if not directory:
        return 0
    elif "," not in directory:
        return 1
    elif "[" in directory:
        return count_files(extract(directory, 0))
    else:
        return 1+count_files(directory[directory.find(",")+1:])
    
def extract(s, start):
    first = s.find("[")
    i = s.find("]", start)
    part = s[first:i+1]
    if part.count("]")<part.count("["):
        x = extract(s, i+1)
        return x
    else:
        a = part.removeprefix("[").removesuffix("]")
        if "[" in a:
            sub_part = extract(a, 0)
            a = a[:a.rfind(",", 0, a.find("["))] + "," + sub_part
        if s.count("[")>part.count("["):
            if "[" not in s[i+2:s[i+2:].find(",")+i+2]:
                x = extract("[" + s[i+2:] + "]", 0)
            else:
                x = extract(s[i+2:], 0)
            return a + "," + x
        else:
            return a