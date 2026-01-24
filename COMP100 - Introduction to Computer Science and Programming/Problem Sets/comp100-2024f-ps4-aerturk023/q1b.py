import math
from q1a import calculate

def derivative(f, x):
    #Separate Summations
    if ")+" in f:
        f = str(derivative(f[:f.find("+")], x)) + f[f.find("+"):]
    if "+s" in f or "+c" in f:
        f = f[:f.find("+")+1] + str(derivative(f[f.find("+")+1:], x))
    
    #Product Rule
    if ")*" in f:
        f = derivative(f[:f.find("*")], x) * calculate(f[f.find("*")+1:], x) + calculate(f[:f.find("*")], x) * derivative(f[f.find("*")+1:], x)
        return f
    
    # The Chain Rule and Taking Derivative
    if "*" not in f and "+" not in f:
        if f.startswith("s"):
            f = f.replace("sin", "cos", 1) + "*" + str(derivative(f[f.find("(")+1:-1], x))
        elif f.startswith("c"):
            f = f.replace("cos", "-sin", 1) + "*" + str(derivative(f[f.find("(")+1:-1], x))
        elif f == "x":
            return "1"
        else:
            return f
        
    
    return calculate(f, x)