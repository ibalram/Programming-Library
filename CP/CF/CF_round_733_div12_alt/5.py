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


class Person:
    def __init__(self, totalAccountBalance=0, age=0, salary=0, numOfDependents=0):
        self.totalAccountBalance = totalAccountBalance
        self.age = age
        self.salary = salary
        self.numOfDependents = numOfDependents

    def keyToCompare(self):
        return [self.totalAccountBalance, self.age, self.salary, self.numOfDependents]

    def __repr__(self):
        return str(self.keyToCompare())

listOfPersons = [Person(0,1,1,2), Person(5,2,5,2), Person(2,42,4,2), Person(0,3,4,2)]

listOfPersons.sort(key = lambda x: x.keyToCompare())
print(listOfPersons)
