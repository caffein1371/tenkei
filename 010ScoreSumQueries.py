##########################################
import io
import sys

_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
A = [0 for i in range(N+1)]
B = [0 for i in range(N+1)]
for i in range(N):
    c,p = map(int,input().split())
    if c==1:
        A[i+1]+=p
    elif c==2:
        B[i+1]+=p
for i in range(N):
    A[i+1]+=A[i]
    B[i+1]+=B[i]

#print (A)
#print (B)


#クエリ
Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    l-=1
    print (A[r]-A[l],B[r]-B[l])
   #print (B[r],B[l])