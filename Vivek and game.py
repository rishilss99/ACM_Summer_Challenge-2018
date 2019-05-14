n = int(input())
len_test_cases = []
test_cases = []
for case in range(n):
    len_test_cases.append(int(input()))
    test_cases.append(list(map(int,input().split())))
print (len_test_cases) #Remove--------------------------------
print (test_cases) #Remove------------------------------------

max_scores=[]

def invert_sum(test_case,init,fin):
    total=sum(test_case)
    for i in test_case[init:fin]:
        if i==1:
            total-=1
        if i==0:
            total+=1
    return total

def score_finder(len,test_case):
    print (len) #Remove------------------------------------
    print(test_case) #Remove-------------------------------
    temp=[]
    for i in range(1,len):
        k=0
        while k<=(len-i):
            temp.append(invert_sum(test_case,k,k+i))
            k+=1
    print (temp)  #Remove----------------------------------
    return max(temp)


for i in range(n):
    max_scores.append(score_finder(len_test_cases[i],test_cases[i]))
print(*max_scores,sep="\n")




