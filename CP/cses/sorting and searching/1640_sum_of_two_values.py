
import bisect as s
y = lambda :map(int,input().split())
n,x = y()
b = sorted(enumerate(y()), key = lambda x:x[1])
b,a = zip(*b)
r = "IMPOSSIBLE"
for v,i in zip(a,b):
    j = s.bisect_left(a,x-v)
    if j<n and a[j]==x-v and i!=b[j]:
        r = str(i+1)+" "+str(b[j]+1)
print(r)
