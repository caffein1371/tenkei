##########################################
import io
import sys

_INPUT = """\
7 18
7 2
1 6
5 2
1 3
7 6
5 3
5 6
5 4
1 7
2 6
3 4
5 1
4 7
4 6
5 7
3 2
4 2
1 4



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
G =[[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
ans = 0
#print (G)
for i in range(N):
    temp = 0
    for v in G[i]:
        if i>v:
            temp+=1
    if temp==1:
        ans+=1
print(ans)