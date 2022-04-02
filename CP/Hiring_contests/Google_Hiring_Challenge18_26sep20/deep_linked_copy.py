import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------





def deepCopy(head):
    if not head: return None
    mp = {}
    cur = head
    while cur:
        mp[cur] = ALNode(cur.value,None,None)
        cur = cur.next
    cur = head
    while cur:
        if cur.next: mp[cur].next = mp[cur.next]
        if cur.arbitrary: mp[cur].arbitrary = mp[cur.arbitrary]
        cur = cur.next
    return mp[head]
