# a = [1, 2, 1]
#
# b = a
#
# print(b is a)
# nums = [0,2,1,5,3,4]
# # [0,1,2,4,5,3]
# output = []
# for i in range(0, len(nums)):
#     output.append(nums[nums[i]])
# print(output)
# nums = [7,1,5,4,3,4,6,0,9,5,8,2]
# nums = [0,1,1,0]
# nums = [0, 3, 2, 1, 3, 2]
from collections import Counter

# num = Counter(nums)
# ans = []
# for key, value in num.items():
#     if value == 2:
#         ans.append(key)
# print(ans)
#
# lst = []
# for i in set(nums):
#     if nums.count(i) == 2:
#         lst.append(i)
# print(lst)
# output = []
# words = ["leet","code"]
# x = "e"
# for i in range(len(words)):
#    for j in words[i]:
#        # print(j)
#        if j==x:
#         output.append(i)
#         break
# print(output)
# s = "abccbaacz"
# seen = set()
# for char in s:
#     if char in seen:
#         print(char)
#     seen.add(char)
# print("")
# nums = [1,2,3,4]
# print(nums[1]+nums[0])
# Output: [1,3,6,10]
# ans = []
# for i in range(1, len(nums)):
#     nums[i] = nums[i-1] + nums[i]
# print(nums)
num = "1210"
a = Counter(num)
print(a)
for i in range(len(num)):  # 0, 1, 2, 3
    if a[str(i)] != int(num[i]):
        print(False)
print(True)
# s = "tree"
# a = Counter(s)
# print(a)

# num = "1200"
# print(num[0])
        ````    ```````````````````````