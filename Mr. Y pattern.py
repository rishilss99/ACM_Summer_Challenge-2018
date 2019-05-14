n = int(input())
i=1
while i<=n:
    print('*'*i)
    i+=1
i-=1
"""Insert code for the pattern of alphabets here"""
for j in range(n):
    print('Z',end=' ')
    for k in range(j):
        print(chr(89-k),end=' ')
    for l in range(n -j-1):
        print(chr(65+l),end=' ')
    print('',end='\n')

while i>=1:
    print('*'*i)
    i-=1