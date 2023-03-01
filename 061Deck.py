##########################################
import io
import sys

_INPUT = """\
6
1 1000000000
2 200000000
1 30000000
2 4000000
1 500000
3 3






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
from collections import deque
d = deque([])
for i in range(N):
    t,x = map(int,input().split())
    if t == 1:
        d.appendleft(x)
    elif t==2:
        d.append(x)
    elif t==3:
        print (d[x-1])
    
