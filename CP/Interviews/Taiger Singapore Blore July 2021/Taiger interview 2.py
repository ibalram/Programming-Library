"""
Applied Via LinkedIn:
Junior Software Engineer
Taiger: Singapore (remote) soon-bangalore

HR (Roshini N) contacted


Monday 19-07-2021
Intro Session (HR round)
10:30Am - 11:00am  - google meet
---------------------------------

Intro
Why leaving Capgemini?
Can you cop up with remote international team?
java questions:

4 oops elements
annotations
exception handeling

About quick/brief discussion projects


"""











# Round 2 - Technical Arvin Acerna
# Staff SWE - 9 years Exp.
# 10:00Am-11:00Am
# Intro




# https://codeshare.io/OdNdBr



# Find move all the zeros to end of array preserving the order of others
# O(n), O(n) count zeros
# O(n), O(1) two pointers, just pushing all the non zeros to the left






# You are given a string s consisting of characters: (, ), [, ], { and }. Write a program to check whether the characters in the string s are valid or not.
# Problem Note:

# A string if said to be valid if an open parenthesis is closed by the same type of parenthesis.
# Also, the open parenthesis must be closed in the correct order.
# Return 1, if the string is valid, else return 0.
# Example 1
# Input: "(([](){}))"
# Output: 1
# Explanation: In the above example, every parenthesis and bracket has opening and closing in the correct order. Thus, we get 1(true) as output.


# time: O(n)
# space: O(n)
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


# (([](){}))




"""
Java Questions:

4 Oops elements:

Some Annotations
design patterns Singleton
builders design pattern
limitation of inheritance

Scope of bean - prototype, singleton(default)
REST api




"""
