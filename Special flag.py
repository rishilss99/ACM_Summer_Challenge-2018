import sys
p,q=input().split()
p,q=int(p),int(q)
main=[]
for i in range(p):
    main.append("".join(list(map(str,input().split()))))
print(main) #Remove
countver = []

for j in main:
    r, g, w = 0, 0, 0
    r+=j.count('R')
    w+=j.count('W')
    g+=j.count('G')
    countver.append([r,w,g])
    for i in j:
        if i not in ['R','W','G']:
            print('NO')
            sys.exit(0)
print (countver) #Remove

"""Total no. of elements"""
def sum_total(in_list):
    r,w,g=0,0,0
    for i in in_list:
        r+=i[0]
        w+=i[1]
        g+=i[2]
    if (r==w==g):
        return True
    else:
        return False

"""Case for vertical stripes"""
def checkver(in_list):
    if q%3!=0:
        return False
    k=1
    while in_list[k]==in_list[k-1]:
        if k==(p-1): #Replaced len(in_list) by p
            return True
        else:
            k+=1
    return False

"""Case for horizontal stripes"""
def checkhor(in_list):
    if p%3!=0:
        return False
    if p==3:
        if sorted(countver)==[[0, 0, q], [0, q, 0], [q, 0, 0]]:
            return True
        else:
            return False
    for i in range(0,p,p//3):
        k=i+1
        while k<(i+p//3):
            if in_list[k]!=in_list[k-1]:
                return False
            else:
                k+=1
            if k==p:
                return True

if (sum_total(countver) and (checkver(main) or checkhor(main))):
    print('YES')
else:
    print('NO')








