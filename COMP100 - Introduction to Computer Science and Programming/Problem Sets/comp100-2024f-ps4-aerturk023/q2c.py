def largest_file(directory):
        
        
    if not directory:
        return 0
    elif "[" in directory:
        return largest_file(extract(directory, 0))
    if "," not in directory:
        return directory[:directory.find("(")]
    if int(directory[directory.find("(")+1:directory.find(")")]) > int(directory[directory.find("(", directory.find(","))+1:directory.find(")", directory.find(","))]):
        return largest_file(directory.replace(directory[directory.find(","):directory.find(")", directory.find(","))+1], ""))
    else:
        return largest_file(directory.replace(directory[:directory.find(")")+2], ""))
    
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
