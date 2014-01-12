def nWheels(x):
    if x==0:
        return 0
    else:
        return 4+nWheels(x-1)
print nWheels(3)
