##########################################
import io
import sys

_INPUT = """\
10 1 0
0 0 0 0 0 0 0 0 0 0



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,P,Q = map(int,input().split())
Alist = list(map(int,input().split()))

import itertools
ans = 0
for i in itertools.combinations(Alist,5):
    #最後に１回割るとTLE
    #数が大きくなりすぎてしまうため
    if i[0]%P*i[1]%P*i[2]%P*i[3]%P*i[4]%P==Q:
        ans+=1
print (ans)