def nTriangle(x):
    if (x==1):
        return 1
    return x + nTriangle(x-1)
print nTriangle(6)
