import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)

mod = int(1e9+7)


# https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Left_index(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn

def orientationH(p, q, r):
    '''
    To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    '''
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convexHull(points, n):
    if n < 3:
        return []
    l = Left_index(points)
    hull = []
    p = l
    q = 0
    while(True):
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if i==p or i==q: continue
            if(orientationH(points[p], points[i], points[q]) == 2):
                q = i
        p = q
        if(p == l):
            break
    res = []
    for each in hull:
        res.append([points[each].x, points[each].y])
    return res

INT_MAX = 10000000
def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
    if ((q[0] <= max(p[0], r[0])) &
        (q[0] >= min(p[0], r[0])) &
        (q[1] <= max(p[1], r[1])) &
        (q[1] >= min(p[1], r[1]))):
        return True
    return False

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are colinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p:tuple, q:tuple, r:tuple) -> int:
    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))
    if val == 0:
        return 0
    if val > 0:
        return 1 # Collinear
    else:
        return 2 # Clock or counterclock

def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True
    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True
    return False

def is_inside_polygon(points:list, p:tuple) -> bool:
    n = len(points)
    if n < 3:
        return False
    extreme = (INT_MAX, p[1])
    count = i = 0
    while True:
        next = (i + 1) % n
        # Check if the line segment from 'p' to
        # 'extreme' intersects with the line
        # segment from 'polygon[i]' to 'polygon[next]'
        if (doIntersect(points[i], points[next], p, extreme)):

            # If the point 'p' is colinear with line
            # segment 'i-next', then check if it lies
            # on segment. If it lies, return true, otherwise false

            if orientation(points[i], p, points[next]) == 0:# and onSegment(points[i], p, points[next]):
                return False
            count += 1
        i = next
        if (i == 0):
            break
    return (count % 2 == 1)

def dist(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
# https://www.geeksforgeeks.org/area-of-a-polygon-with-given-n-ordered-vertices/
def polygonArea(hull, n):
    res = 0
    for i in range(n):
        j = (i+1)%n
        res+=dist(hull[i],hull[j])
    return res

for _test in range(int(input())):
    res = float("inf")
    n = int(input())
    a = [ilist() for i in range(n)]
    x,y = imap()
    for mask in range(1<<n):
        points = []
        for i in range(n):
            if mask>>i&1:
                points.append(Point(*a[i]))
        hull = convexHull(points, len(points))
        if is_inside_polygon(hull, (x,y)):
            area = polygonArea(hull, len(hull))
            # if area<res:
            #     print(area, hull)
            res = min(res, area)
    if res==float("inf"):
        res = "IMPOSSIBLE"
    print('Case #{}:'.format(_test+1), res)

