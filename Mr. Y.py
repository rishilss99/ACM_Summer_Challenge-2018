import sys
n = int(sys.stdin.readline())
l=[]
new=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for each in l:
    k=0
    total = each[1]
    while(total + (k+1)*3<=360) and ((k+1)<=each[0]):
        k+=1
        total+=k*3
    new.append(k)
print(*new,sep="\n")
