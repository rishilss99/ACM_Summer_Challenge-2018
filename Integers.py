"""lines = []
new=[]
while True:
    line = input()
    if line:
        lines.append(str(line))
    else:
        break
for each in lines:
    if each[len(each)-1]=='0':
        new.append(each)
print(*new,sep="\n")"""

acc = []
out = ''
while True:
    try:
        acc.append(input(''))
    except EOFError:
        out = '\n'.join(acc)
        break
print (acc)