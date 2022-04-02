# https://atcoder.jp/contests/abc223/tasks/abc223_f
# https://atcoder.jp/contests/abc223/submissions/26670707

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

class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)




n,q = imap()
s = list(input().strip())
a = [0]*n
a[0] = 1 if s[0]=="(" else -1
for i in range(1,n):
    a[i] = a[i-1]
    a[i] += 1 if s[i]=="(" else -1
st = LazySegmentTree(a,float('inf'),min)
# print(st)
for _ in range(q):
    t,x,y = imap()
    x-=1
    y-=1
    if t==1:
        if s[x]==s[y]:continue
        if s[x]=="(":
            st.add(x,y,-2)
        else:
            st.add(x,y,2)
        s[x],s[y] = s[y],s[x]
    else:
        mn = st.query(x,y+1,float("inf"))
        if x==0:left = 0
        else: left = st.query(x-1,x, float("inf"))
        right = st.query(y,y+1,float("inf"))
        if left==right and mn==left:
            print("Yes")
        else:
            print("No")



"""
Good Bye and Take Care!
External
Inbox

Anju Uralath <anju.uralath@johnlewis.co.uk>
Wed, 27 Oct, 16:19 (1 day ago)
to anju.uralath

Hello All,

As you might already know today is my last working day with the Partnership.

Before signing off, I would like to thank everyone for your support and encouragement during our time together. 

I want to convey my gratitude to my mentors and leads – Dan and Chris for continuously encouraging me and providing me with opportunities that helped me grow both professionally and personally. I want to thank my amazing teammates Martin, Mike, Ramon and Rasika who were very kind to me and for all the things I got to learn from them.

Wishing you all a happy and healthy life! Stay safe & stay in touch. :)

Let's connect here:
LinkedIn - https://www.linkedin.com/in/anju-uralath/
Personal mail - anju.uralath@gmail.com   

Regards,
Anju Uralath
+91 984 058 2277 












Thank you and good bye!!!
Inbox

Logi Krishnamoorthy logeswari.krishnamoorthy@waitrose.co.uk via johnlewis.co.uk Unsubscribe
Fri, 17 Sept, 17:37
to

Hi all,

Just sending a quick note to say goodbye as I will be finishing my journey in Partnership today.  Eight years have gone in a flash. I don't even know where to start a goodbye off to this amazing team.    

A massive thank you to everyone across the partnership  for making me feel so welcomed over these years.  I am so proud to leave knowing I was part of such a successful, passionate, motivated team and can honestly say its been a pleasure to have been on that journey with you all. I have enjoyed every minute and made countless memories.

Thank you for all your help and support and most importantly for all the friendship and laughs!

I really do wish you all every success in everything you do and would welcome staying in touch via LinkedIn or email.

Thanks for all your kind words, flowers and the leaving presents. 


Kind Regards
Logi Krishnamoorthy
Test Engagement & Delivery Lead
Technology & Change

Phone: 07527827608 
Email:logeswari.krishnamoorthy@gmail.com






"""
