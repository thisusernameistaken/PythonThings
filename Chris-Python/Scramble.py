
import itertools
words=open("text1.txt","r")
thing = str(raw_input())
arr=[]
jarr=[]
for z in words:
    arr.append(z.rstrip())
x=3
print "Loading..."
while (x<=len(thing)):
    for word in list(map("".join, itertools.permutations(thing,x))):
        word=word.upper()
        if word in arr:
            jarr.append(word.rstrip())
    x+=1

jarr.sort()
print "---RESULTS---"
for h in jarr:
    print h
