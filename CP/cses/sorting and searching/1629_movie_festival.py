
a = sorted([list(map(int,input().split())) for i in range(int(input()))], key=lambda x:x[1])
l=r=0
for s,e in a:
    if s>=l:
        r+=1
        l = e
print(r)
