'''
Problem Statement:
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

'''

def subarray(nums, target):
    min_val = float('infinity')
    total = 0
    numsStart = 0
    for val in range(len(nums)):
        total += nums[val]
        while total >= target:
            min_val = min(min_val, val - numsStart + 1)
            total -= nums[numsStart]
            numsStart += 1
    if min_val == 'infinity':
        return 0
    return min_val

print(subarray([2, 1, 5, 2, 3, 2], 7))
print(subarray([2, 1, 5, 2, 8], 7))
print(subarray([3, 4, 1, 1, 6], 8))


