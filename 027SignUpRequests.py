N = int(input())
S = []
temp = set()
for i in range(N):
    s = input()
    s = ''.join(s)
    temp1 = len(temp)
    temp.add(s)
    if temp1<len(temp):
        print (i+1)
#print (temp)    