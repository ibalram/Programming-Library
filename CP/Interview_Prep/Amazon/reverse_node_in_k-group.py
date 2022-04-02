# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]

# Input: head = [1], k = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz



"""

'''

res = 0
    jump

k = 3
          |
   A->B->C->D->E->F
          |
   l        r
   cur     pre

   iter1
          |
D<-A  B->C->D->E->F
   ^  ^   |
   l  ^     r
 pre  cur

   iter2
          |
D<-A<-B  C->D->E->F
      ^  ^|
   l  ^  ^  r
    pre  cur

   iter3
           |
D<-A<-B<-C  D->E->F
         ^ |^
   l     ^  r
       pre  cur

--------------------
           |
D<-A<-B<-C  D->E->F
   ^     ^ |^
   ^     |  l
 jump    0  cur

'''
As we go naively we can first extract list then perform reversal and then update values.
but this way requires O(n) extra space.

we can do this by maintaining two reference variables cur and prev.
Update prev = cur and cur = cur.next simultanously in a loop of length k

l,r = define range of reversal
pre, cur: pointers used in standard reversal method
jump: Used to connect last k-group to first node in following k-group

Time complexity: O(n)
Space complexity: O(1)
`

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        r = head
        l = head
        res = ListNode(0)
        res.next = head
        jump = res
        while True:
            count = 0
            while r and count<k:
                r = r.next
                count+=1
            if count==k:
                cur,prev = l,r
                for i in range(k):
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                jump.next = prev
                jump = l
                l = r
            else:
                return res.next



