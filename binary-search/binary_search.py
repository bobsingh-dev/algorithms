# Question:

"""
Given a sorted list of up to 100,000 unique integers and a target,
return the target's index. Return -1 if the target is not found.

The list is sorted in ascending order and may be empty.

Example: nums = [1, 3, 5, 7, 9], target = 7 → 3

Pattern: Binary Search

"""


def binary_search(nums: list[int], target: int) -> int:
  left = 0  # start at first index
  right = len(nums) -1  # start at last index

  while left <= right:  #continue while there are positions to check
    middle = (left + right) //2  # find the middle index

    if nums[middle] == target:
      return middle

    if nums[middle] < target:  # target must be to right
      left = middle + 1

    else:    # target must be to the left
      right = middle -1

  return -1   # target not in list


if __name__ == "__main__":
  assert binary_search([1, 3, 5, 7, 9], 7) == 3
  assert binary_search([], 7) == -1
  print("Both checks passed")



# Time: O(log n)
# Extra Space: O(1)
