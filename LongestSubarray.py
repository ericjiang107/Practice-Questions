'''
Problem Statement 
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest 
contiguous subarray having all 1s.

Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

def longestSubArray(nums, k):
    count_ones = 0
    window_start = 0
    max_length = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count_ones += 1
        if (i - window_start + 1 - count_ones) > k:
            if nums[window_start] == 1:
                count_ones -= 1
            window_start += 1
        max_length = max(max_length, i - window_start + 1)
    return max_length

print(longestSubArray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
