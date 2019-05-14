import sys
n=int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
q = int(sys.stdin.readline())
for i in range(q):
    x,l,r=[int(x) for x in sys.stdin.readline().rstrip().split()]
    print(arr[l-1:r].count(x))
