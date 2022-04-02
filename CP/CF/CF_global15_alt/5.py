import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)





# https://codeinterview.io/ETZLPSTKCN




# function func2(){
#   for(let i = 0; i < 3; i++){
#     setTimeout(()=> console.log(i),2000);
# }

# }

# func2();

# // 0 1 2

# // main

# // // event_loop

# // console.log(i)
# // console.log(i)
# // console.log(i)
