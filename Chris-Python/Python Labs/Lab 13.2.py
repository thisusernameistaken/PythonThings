def countVowels(s):
    z=s
    z=z.lower()
    z=str(z)
    z[1:]
    x=0
    if(z[0]=='a')or (z[0]=='e')or(z[0]=='i')or(z[0]=='o')or(z[0]=='u'):
        x+=1
    if (len(s)==1):
        return x
    return x + countVowels(z[1:])
print countVowels("HER")
