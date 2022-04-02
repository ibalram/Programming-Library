

# def solution(s):
#     count = 1
#     n = len(s)
#     result = []
#     for i in range(1,n):
#         if s[i]==s[i-1]:
#             count+=1
#         else:
#             result.append(str(count)+s[i-1])
#             count = 1
#     result.append(str(count)+s[n-1])
#     return ", ".join(result)

# # # a a a b b d d a a b b c c
# #           i
# # # count = 1
# # # result = ["3a"]

# print(solution("aaabbddaabbcc")=="3a, 2b, 2d, 2a, 2b, 2c")



# Balanced String:
# // isBalanced(""[{()}]"") - true
# // isBalanced(""[({(})]"") - false
# // isBalanced(""{[}"") - false"

# a = [{()}] = [b]
# b = {()}
# c = ()
# isBalanced("[{()}]"") = (first_is_matched_with last && isBalanced("{()}")
