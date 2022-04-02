input()
a = list(map(int,input().split()))
s = set()
l = r =0
for i in a:
    while i in s:
        s.remove(a[l])
        l+=1
    s.add(i)
    r = max(r,len(s))
print(r)
