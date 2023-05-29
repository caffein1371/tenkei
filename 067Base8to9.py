import sys, io, time
# Sample Input
Input = '''\
21 1



'''
sys.stdin = io.StringIO(Input)
Start = time.time()
# Source Code
N,K = map(int,input().split())

print (N)
# for i in range(K):

#     while N<=9:
#         N

# Exec Time
End = time.time()
Exec = End - Start
print(f'{int(Exec * 1000)} ms')