# Question:

"""

Given a list of up to 100,000 integers, return True if any value
appears at least twice. The list may be empty.

Pattern: Set Membership

"""

def contains_duplicate(nums: list[int]) -> bool:  # Take list of integers and return True or False

    seen = set() # Create empty set to begin tracking numbers already visited

    for num in nums:      # read each number in list from left to right
        if num in seen:   # did we already see number
            return True   # we found a duplicate, so stop

        seen.add(num) # remember this number for other iterations

    return False  # no duplicates found in list



if __name__ == "__main__":
    assert contains_duplicate([1, 2, 1]) is True
    assert contains_duplicate([]) is False
    print("Both checks passed.")




# Time: O(n) on average
# Extra Space: O(n) in the worst case


