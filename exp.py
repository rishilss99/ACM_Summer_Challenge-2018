import sys
a = [1,2,4]
b = [1,2,4]
if a==b:
    print (True)

print(list(range(0,1)))
a = [[3,0,0],[0,0,3],[0,3,0]]
print (sorted(a))

print([1,2,3]+[4,5,6])
main = ['RRR','WWW','QQQ']

for i in range(0,18,18//3):
    print (i)

a =[[1,0,1],0,1]
print (a[0][1:2])

a = set()
a.add((1,0))
a.add((1,0))
print (a)
a=list(a)
a[0]=list(a[0])
print (sum(a[0]))
