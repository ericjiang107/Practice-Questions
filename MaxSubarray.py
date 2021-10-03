'''
Problem Statement:
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def maxArray(nums, count):
    max_sum = 0
    total_sum = 0
    numsStart = 0
    for val in range(len(nums)):
        total_sum += nums[val]
        if val >= count-1:
            max_sum = max(max_sum, total_sum)
            total_sum -= nums[numsStart]
            numsStart += 1
    return max_sum

print(maxArray([2, 1, 5, 1, 3, 2], 3))
