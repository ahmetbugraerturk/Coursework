import math

def calculate(f, x):
    if ")+" in f:
        f = str(calculate(f[:f.find("+")], x)) + f[f.find("+"):]
    if "+s" in f or "+c" in f:
        f = f[:f.find("+")+1] + str(calculate(f[f.find("+")+1:], x))
    if ")*" in f:
        f = str(calculate(f[:f.find("*")], x)) + f[f.find("*"):]
    if "*s" in f or "*c" in f:
        f = f[:f.find("*")+1] + str(calculate(f[f.find("*")+1:], x))
        
    if "sin(x)" in f:
        return calculate(f.replace("sin(x)", "x", 1), math.sin(x))
    elif "cos(x)" in f:
        return calculate(f.replace("cos(x)", "x", 1), math.cos(x))
    
    elif "+" not in f and "*" in f:
        f = float(f.split("*")[0]) * float(f.split("*")[1])
    elif "+" in f and "*" not in f and "x" not in f:
        summ = float(f[:f.find("+")]) + float(f[f.find("+")+1:][:f[f.find("+")+1:].find("+")])
        f = str(summ) + f[f.find("+")+1:][f[f.find("+")+1:].find("+"):]
        return calculate(f, x)
    
    elif f == "x":
        return x
    elif f == "-x":
        return -x
    
    return float(f)
    
