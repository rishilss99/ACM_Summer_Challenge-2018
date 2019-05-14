import sys
a = sys.stdin.readline()
transtab = str.maketrans("","","aeiou")
sys.stdout.write(a.translate(transtab))

