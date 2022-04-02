input()
b = [-1<<34]
for i in map(int,input().split()):b.append(max(i,b[-1]+i))
print(max(b))
