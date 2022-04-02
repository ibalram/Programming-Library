def two(n,a):
    st = set(a)
    ast = set()
    for i in a:
        ast.add(i[0])
    # mp = {}
    # smp = {}
    # scnt = {}
    # for i in a:
    #     if i[1:] not in mp:
    #         mp[i[1:]] = set()
    #     if i[0] not in smp:
    #         smp[i[0]] = set()
    #     for j in ast:
    #         if j+i[1:] not in st and j!=i[0]:
    #             mp[i[1:]].add(j+i[1:])
    #             scnt[j] = scnt.get(j,0)+1
    #             smp[i[0]].add(j+i[1:])


    # # ln =len(mp)
    # # print(mp)
    # # res = ln*(ln-1)
    # res = 0
    # # print(mp)
    # # print(smp)
    # cc = n
    # for i in mp.keys():
    #     if len(mp[i]):cc = min(cc,len(mp[i]))
    #     val = 0
    #     for j in mp[i]:
    #         if j[0] in smp:
    #             val+=len(smp[j[0]])
    #     if len(mp[i]):res+=val

    mp = {}
    for i in a:
        if i[1:] not in mp:
            mp[i[1:]] = [i[0]]
        else:
            mp[i[1:]].append(i[0])
    res = 0
    for i in mp.keys():
        for j in mp.keys():
            if i==j: continue
            cand = set(mp[i]+mp[j])
            res+=(len(cand)-len(mp[i]))*(len(cand)-len(mp[j]))
    return res
    # for i in range(n):
    #     for j in range(n):
    #         if a[i][0]!=a[j][0] and a[i][1:]!=a[j][1:] and a[i][0]+a[j][1:] not in st and a[j][0]+a[i][1:] not in st:
    #             res+=1
    # print(res)
    # return res//cc,mp,smp

def one(n,a):
    st = {}
    for i in a:
        if i not in st: st[i] = 1
        else: st[i]+=1
    res = 0
    for i in range(n):
        for j in range(n):
            if a[i][0]!=a[j][0] and a[i][1:]!=a[j][1:] and a[i][0]+a[j][1:] not in st and a[j][0]+a[i][1:] not in st:
                res+=1
    # print(res)
    return res
from random import *

tt = 100
for _ in range(tt):
    n = randint(1,100)
    a = ["".join(chr(ord("a")+randint(0,25)) for i in range(randint(2,5))) for j in range(n)]

    a = list(set(a))
    n = len(a)
    res1 = one(n,a)
    res2 = two(n,a)
    if res1!=res2:
        print("correct:",res1)
        print("wrong:",res2)
        # print(mp)
        # print(smp)
        print(n)
        print(*a)
        break

