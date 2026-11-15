"""
Given a list of up to 100,000 integers, move all zeroes to the end
while keeping the other numbers in their original order.

Modify the list in place. Do not create another list.
The list may be empty.

Example: [0, 1, 0, 3, 12] becomes [1, 3, 12, 0, 0]

Pattern: In-Place Rearrangement — Read/Write Pointers


"""


def move_zeroes(nums: list[int]) -> None:
    write = 0 # track where the next nonzero number belongs

    for read in range(len(nums)):   # read each position from left to right
        if nums[read] != 0:    # keep nonzero numbers
            nums[write] = nums[read]   # place this number at the write position
            write += 1    # advance to the next write position


    for index in range(write, len(nums)):    # visit the remaining positions
        nums[index] = 0         # fill them with zeroes



# Testing With Assertions
if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    move_zeroes(numbers)
    assert numbers == [1, 3, 12, 0, 0]

    empty: list[int] = []
    move_zeroes(empty)
    assert empty == []

    print("Both checks passed.")



# Time: O(n)
# Extra Space: O(1)
