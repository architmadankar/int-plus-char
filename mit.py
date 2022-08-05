fp = open("sample.txt","r")
m="@mitwpu.edu.in"
sum=""
mylist=[]

data=fp.read().splitlines() 
for ch in data:

    sum=ch+m
    mylist.append(sum)

print(mylist, end ="\n")
for x in mylist:
    print(x)
