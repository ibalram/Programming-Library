"""
Applied via instahyre
Java Developer- 1+ Exp


Tuesday 20-07-2021
Call from Nikitaseles Pinto
basic Intro and discussion
Scheduled Interview round 1




"""


# HashedIn Interview round 1
# 22-07-2021 (11:00Am-11:45 Am)
# Interviewer: Chakresh tiwari(SWE2), Someshwar Bhale, SHara Rizvi




# https://docs.google.com/document/u/1/d/1CRqVFXRGBnINN2U0xCDs9utjJvx-3N4PWic72RawH08/edit
# https://codeinterview.io/JHSSRBBBBX


# Find the max sum subarray
def solve(arr):
  n = len(arr)
  curSum = arr[0]
  result = arr[0]
  for i in range(1,n):
    curSum = max(curSum+arr[i], arr[i])
    result = max(result, curSum)
  return result


print(solve([ -2, -3, 4, -1, -2, -1, 5, -3]))

# Time complexity: O(n)
# Space complexity: O(1)


# Find the run-length encoding
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



# Find second Max Integer in array
# 3 approaches:
#   1. Sorting O(nlogn)
#   2. Keeping two avariables O(n)
#   3. Using heap: i) O(n + logn) ii) O(n*log2)~O(n)

# Sort an array which consists only 0,1 and 2
# 3 approaches:
#   1. Sorting O(nlogn)
#   2. count sort(couting 0s,1s and 2s) O(n) - 2 iterations
#   3. two pointers O(n) - single iteration - inplace swapings


"""
Java Questions:

Inversion of Control
Java 8 features: stream,
4 enders in stream



"""
