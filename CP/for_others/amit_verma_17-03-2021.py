def solution1(S,C):
    cur = C[0]
    res = 0
    for i in range(1,len(S)):
        if S[i]==S[i-1]:
            cur=max(cur, C[i])
        else:
            res+=cur
            cur = C[i]
    res+=cur
    return sum(C)-res

# print(solution1("abccbd",[0,1,2,3,4,5]))
# print(solution1("aabbcc",[1,2,1,2,1,2]))
# print(solution1("aaaa",[3,4,5,6]))
# print(solution1("ababa",[10,5,10,5,10]))


def solution2(blocks):
    peaks = [0]
    res =0
    n = len(blocks)
    lst = {}
    for i in range(1,n-1):
        if i>0 and i<n-1 and blocks[i-1]<=blocks[i]>=blocks[i+1]:
            peaks.append(i)
    peaks.append(n-1)
    lst[blocks[peaks[0]]] = 0
    for i in range(1,len(peaks)):
        block = blocks[peaks[i]]
        pre_block = blocks[peaks[i-1]]
        if peaks[i]!=peaks[i-1]+1 or peaks[i] in [1,n-1] and block!=pre_block:
            lst[block] = i
        res = max(peaks[i]-peaks[lst[pre_block]]+1, res)
    return res

def solution(blocks):
    ranges = []
    l = 0
    val = blocks[0]
    n = len(blocks)
    for i in range(1,len(blocks)):
        if blocks[i]!=blocks[i-1]:
            ranges.append([val,l,i-1])
            l = i
            val = blocks[i]
    ranges.append([val,l,n-1])

    peaks = [0]
    res =0
    n = len(ranges)
    for i in range(1,n-1):
        pre = ranges[i-1][0]
        cur = ranges[i][0]
        nxt = ranges[i+1][0]
        if i>0 and i<n-1 and pre<cur>nxt:
            peaks.append(i)
    peaks.append(n-1)
    for i in range(1,len(peaks)):
        pre = ranges[peaks[i-1]][1]
        cur = ranges[peaks[i]][2]
        res = max(cur-pre+1, res)
    return res
    # lst[blocks[peaks[0]]] = 0
    # for i in range(1,len(peaks)):
    #     # block = blocks[peaks[i]]
    #     # pre_block = blocks[peaks[i-1]]
    #     if peaks[i]!=peaks[i-1]+1 or peaks[i] in [1,n-1] and block!=pre_block:
    #         lst[block] = i
    #     res = max(peaks[i]-peaks[lst[pre_block]]+1, res)
    # return res

print(solution([2,6,8,5]))
print(solution([1,5,5,2,6]))
print(solution([1,1]))
print(solution([1,2,5,1,1,1,6]))





