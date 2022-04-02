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


import time, math
sTime = time.time()

from random import *
# seed(randint(1,10000))
seed(531)
asci = "abcdefghijklmnopqrstuvwxyz"

N,K = imap()
s = input().strip()

# N,K = 1000, randint(50,100)
# s = "".join(asci[randint(0,25)] for i in range(N))


bestCut =[]
bestOrder = []
bestScore = 0
bestFlip = [0]*(K)

cut = []
order = []
flip = bestFlip[:]
score = 0

def getScore():
    lst = 0
    string = []
    for i in order:
        pos = cut[i]
        lst = 0
        if i>0: lst = cut[i-1]
        strng = s[lst:pos]
        string.append(strng[::-1] if flip[i] else strng)
    string ="".join(string)
    cnt = 0
    # print(cut)
    # print(order)
    # print(string)
    def expand(l,r):
        nonlocal cnt
        while l>=0 and r<N and string[l]==string[r]:
            l-=1
            r+=1
            cnt+=1
    for i in range(N):
        expand(i,i)
        expand(i,i+1)
    score = cnt*(bestFlip.count(0)+1)
    return score

def save(score, cut,order,flip=bestFlip):
    global bestScore, bestCut, bestOrder, bestFlip
    if score>bestScore:
        bestScore = score
        bestCut = cut[:]
        bestOrder = order[:]
        bestFlip = flip[:]

def restore():
    global cut, order, flip
    cut = bestCut[:]
    order = bestOrder[:]
    flip = bestFlip[:]

def printAns():
    for i,j in zip(bestCut,bestFlip):
        print(i,j)
    print(*[i+1 for i in bestOrder])


best = "a"

for i in asci:
    st = set()
    st.add(N)
    pairs = []
    start = 0
    while start<N:
        if s[start] != i:
            start+=1
        else:
            end = start
            # print(N, s)
            while end+1<N and s[end+1]==i:
                end+=1
            pairs.append((end-start+1, start))
            start = end+1
    pairs.sort(reverse = True)
    for size, start in pairs:
        end = start + size-1
        if start>0 and len(st)<K:
            st.add(start)
        if len(st)<K:
            st.add(end+1)
    while len(st)<K:
        st.add(randint(1,N)%N+1)
    order = []
    cut = list(sorted(st))
    mp = defaultdict(list)
    for j in range(K):
        mp[s[(cut[j-1] if j else 0): cut[j]]].append(j)
    for char in asci:
        strng = ""
        for j in range(1,N+1):
            strng+=char
            for k in mp[strng]:
                order.append(k)
            del mp[strng]
    for j in mp.keys():
        for k in mp[j]:
            order.append(k)
    newScore = getScore()
    if newScore>bestScore:
        best = i
        save(newScore, cut, order)
restore()

def simAnneal(choices):
    global sTime, cut, order
    maxTemp, minTemp = 1, 0.1
    change = 0.05
    delta = (sTime+4-time.time())
    sTime = time.time()
    score = getScore()
    temp = maxTemp
    while True:
        ratio = (time.time()-sTime)/delta
        if ratio>1: break
        temp = maxTemp*(minTemp/maxTemp)**ratio
        # print(temp)
        if ratio>change: change+=0.05

        for _ in range(50):
            dummyCut = cut[:]
            dummyOrder = order[:]
            if len(choices) and K>2:
                x = randint(0,K-2)
                y = randint(0,len(choices)-1)
                cut[x], choices[y] = choices[y], cut[x]
                cut.sort()
            for i in range(5):
                if K>1:
                    x = randint(0,K-1)
                    y = randint(0,K-1)
                    if x==y: continue
                    order[x], order[y] = order[y], order[x]
            newScore = getScore()
            # print(newScore, score)
            try:
                lim = math.exp((newScore-score)/temp)
            except:
                lim = float("inf")
            if newScore<=score or random()<= lim:
                save(newScore,cut, order)
                score = newScore
            else:
                order = dummyOrder[:]
                cut = dummyCut[:]
choices = []
for i in range(1,N):
    if s[i]==best or s[i]!=s[i-1] and s[i-1]==best:
        if i not in cut:
            choices.append(i)
simAnneal(choices)

restore()
for i in range(50):
    if k>1:
        x = randint(0,K-1)
        flip[x]^=1
        save(getScore(), cut, order,flip)
printAns()




# while time.time()-sTime<=2:
#     x = randint(0,K-1)
#     y = randint(0,k-1)
#     order[x],order[y] = order[y],order[x]
#     save(getScore(), cut,order)
#     restore()
# printAns()


