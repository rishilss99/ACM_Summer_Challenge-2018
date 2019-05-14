n = int(input())
len_test_cases = []
test_cases = []
max_length = []
for case in range(n):
    len_test_cases.append(int(input()))
    test_cases.append(list(map(int,input().split())))
    max_length.append(int(input()))


max_sum=[]


for i in range(n):
    maxi=0
    k=0
    m = max_length[i]
    while k<=(len_test_cases[i]-m):
        a=sum(test_cases[i][k:k+m])
        if a>maxi :
            maxi=a
        k+=1
    max_sum.append(maxi)
print(*max_sum,sep="\n")