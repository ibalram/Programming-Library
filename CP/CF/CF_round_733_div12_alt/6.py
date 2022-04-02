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

import time
from functools import partial
from multiprocessing import Pool, cpu_count, Process
from queue import Queue

def searchInFile(word, file):
    found = 0
    with open(file, 'r') as f:
        for line in f:
            if word in line:
                found |= 1
    return file, found

def naive(func, files):
    result = []
    for filename, found in [search(file) for file in files]:
        if found:
            result.append(filename)
    print(result)

def multiProcessing(func, files, numProcesses):
    q = Queue()
    with Pool(numProcesses or cpu_count()+1) as pool:
        for filename, found in pool.imap_unordered(func, files):
            if found:
                q.put(filename)
    print(list(q.get(1) for i in range(q.qsize())))

if __name__=="__main__":
    startTime = time.time()
    n = 0 # number of worker process
    files = ["1.py", "2.py", "3.py", "4.py", "5.py"]
    word = "cnt"
    search = partial(searchInFile, word)

    # naive(search, files)
    multiProcessing(search, files, n)
    print(time.time()-startTime)









https://codeshare.io/OdNdBr




You are given a string s consisting of characters: (, ), [, ], { and }. Write a program to check whether the characters in the string s are valid or not.

Problem Note:

A string if said to be valid if an open parenthesis is closed by the same type of parenthesis.
Also, the open parenthesis must be closed in the correct order.
Return 1, if the string is valid, else return 0.
Example 1

Input: "(([](){}))"
Output: 1
Explanation: In the above example, every parenthesis and bracket has opening and closing in the correct order. Thus, we get 1(true) as output.



time: O(n)
space: O(n)

def solve(string):
    stack = []
  closing = {"(":")", "{":"}", "[":"]"}
  for i in string:
    if i in ["(", "{", "["]:
        stack.append(i)
    else:
        if len(stack)>0 and closing[stack[-1]]!=i:
        stack.pop()
      else:
        return 0
  return 0 if len(stack)>0 else 1


(([](){}))
