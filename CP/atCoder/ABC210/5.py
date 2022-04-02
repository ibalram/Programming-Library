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

if __name__=="__main__":
    listOfPersons = [Person(0,1,1,2), Person(5,2,5,2), Person(2,42,4,2), Person(0,3,4,2)]
    listOfPersons.sort(key = lambda x: x.keyToCompare())
    print(listOfPersons)











# HashedIn Interview round 1





# https://docs.google.com/document/u/1/d/1CRqVFXRGBnINN2U0xCDs9utjJvx-3N4PWic72RawH08/edit
# https://codeinterview.io/JHSSRBBBBX



def solve(arr):
  n = len(arr)
  curSum = arr[0]
  result = arr[0]
  for i in range(1,n):
    curSum = max(curSum+arr[i], arr[i])
    result = max(result, curSum)
  return result


# print(solve([ -2, -3, 4, -1, -2, -1, 5, -3]))

# Time complexity: O(n)
# Space complexity: O(1)



def solve2(string):
  n = len(string)
  count = 1
  result = ""
  for i in range(1,n):
    if string[i]==string[i-1]:
      count+=1
    else:
      result += string[i-1] + str(count)
      count = 1
  if count>0:
    result += string[n-1]+str(count)
  return result

print(solve2("AAABBCCADDDD")=="A3B2C2A1D4")

# Time complexity: O(n)
# Space complexity: O(1)

