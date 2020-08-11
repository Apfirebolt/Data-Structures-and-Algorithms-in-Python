"""
Another method of deleting duplicate elements in an array.
"""


def removeDuplicates(nums):
  if len(nums) == 1:
    return 1

  i = 0
  for j in range(1, len(nums)):
    if (nums[i] != nums[j]):
      i += 1
      nums[i] = nums[j]

  return i + 1


nums = [1, 4, 4, 4, 6, 12, 2, 2, 7, 9]
removeDuplicates(nums)
print(nums)