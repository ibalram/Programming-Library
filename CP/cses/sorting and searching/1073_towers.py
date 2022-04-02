import bisect as s
m = 1<<34
b = [m]*(int(input())+1)
for i in map(int,input().split()):
    b[s.bisect(b,i)]=i
print(b.index(m))
