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

n = 8
a = [-1, -9, 2, -3, 1, -6, 7, 8]
a = [1, 9, 2, 3, 0, 6, 7, 8]

n = 10
a = [1, 2, 3, 4,5,6,7,8,9,10]






# n = int(input())
# a = list(map(int,input().split()))
def solve(n, a):
    def kadane(arr):
        cursm = mxsm = arr[0]
        for i in arr[1:]:
            cursm = max(i, cursm+i)
            mxsm = max(mxsm, cursm)
        # print(mxsm)
        return mxsm

    m = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            m[i][j] = a[i]*a[j]                                                                           #str(a[i])+"*"+str(a[j])
    res = -float("inf")
    for i in range(n):
        arr1 = []
        arr2 = []
        for j in range(i+1):
            if j>i-j: arr1.append(m[i-j][j])
            if ~j>~(i-j): arr2.append(m[~(i-j)][~j])
        if arr1:
            res = max(kadane(arr1),res)
        if arr2:
            res = max(res,kadane(arr2))
    return res
# print(solve(n,a))


dp  ={}

def solve2(n,a):
    res = 0
    def check(l1,r1, l2,r2):
        ln = r1-l1
        res =0
        for i, j in zip(a[l1:r1],reversed(a[l2:r2])):
            res+=i*j
        return res

    res = -float("inf")
    for ln in range(1,n//2+1):
        for i in range(n):
            if i+ln>n: continue
            l1 = i
            r1 = i+ln
            arr1 = a[l1:r1]
            for j in range(i+ln, n):
                if j+ln>n: continue
                l2 = j
                r2 = j+ln
                arr2 = a[l2:r2]
                res = max(res, check(l1,r1,l2,r2))
    return res


from random import *
test = 0
while test<1000:
    test+=1
    n = randint(2,50)
    a = [randint(-100000,100000) for i in range(n)]
    # print(n,a)
    if solve2(n,a)!=solve(n,a):
        print(n,a)

# print(solve(n,a))


# ip: 1 9 2 3 0 6 7 8
# op: 104





# # n = int(input())
# # a = list(map(int,input().split()))
# def solve(n, a):
#     def kadane(arr):
#         cursm = mxsm = arr[0]
#         for i in arr[1:]:
#             cursm = max(i, cursm+i)
#             mxsm = max(mxsm, cursm)
#         return mxsm

#     m = [[0]*n for i in range(n)]
#     for i in range(n):
#         for j in range(i+1,n):
#             m[i][j] = a[i]*a[j]
#     res = -float("inf")
#     # for i in m:
#     #     print(*i)
#     for i in range(n):
#         arr1 = []
#         arr2 = []
#         # for j in range(i+1):
#         #     arr1.append(m[i-j][j])
#         #     arr2.append(m[~(i-j)][~j])
#         # # print(arr1)
#         # # print(arr2)
#         for j in range(i+1):
#             if j>i-j: arr1.append(m[i-j][j])
#             if ~j>~(i-j): arr2.append(m[~(i-j)][~j])
#         # print(arr1)
#         # print(arr2)
#         if arr1:
#             res = max(kadane(arr1),res)
#         if arr2:
#             res = max(res,kadane(arr2))
#     return res
# print(solve(n,a))



# //  @Test
# //  public void givenEmployeeSalary_WhenUpdated_ShouldMatch200Response() throws EmployeePayrollException {
# //      EmployeePayrollData[] arrOfEmp = getEmpList();
# //      EmployeePayrollService EmployeePayrollService;
# //      EmployeePayrollService = new EmployeePayrollService(Arrays.asList(arrOfEmp));
# //
# //      EmployeePayrollService.updateEmployeeSalary("Nikhil", 8000.0, IOService.REST_IO);
# //      EmployeePayrollData employeePayrollData = EmployeePayrollService.getEmployeePayrollData("Nikhil");
# //      Response response = updateEmployeeSalary(employeePayrollData);
# //      int statusCode = response.getStatusCode();
# //      assertEquals(200, statusCode);
# //  }
# //
# //  @Test
# //  public void givenEmployeeData_WhenDeleted_ShouldMatch200Response() {
# //      EmployeePayrollData[] arrOfEmp = getEmpList();
# //      EmployeePayrollService EmployeePayrollService;
# //      EmployeePayrollService = new EmployeePayrollService(Arrays.asList(arrOfEmp));
# //
# //      EmployeePayrollData employeePayrollData = EmployeePayrollService.getEmployeePayrollData("Nikhil");
# //      Response response = deleteEmployee(employeePayrollData);
# //      int statusCode = response.getStatusCode();
# //      assertEquals(200, statusCode);
# //
# //      EmployeePayrollService.deleteEmployee("Nikhil", IOService.REST_IO);
# //      long entries = EmployeePayrollService.countEntries(IOService.REST_IO);
# //      assertEquals(5, entries);
# //  }
