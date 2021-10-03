# Sliding Window technique:

# ex: finding max sum of any contiguous subarray of size k
# array = [2, 3, 4, 1, 5], k = 3

# have a max variable = 0
# have a total = array[index] 

def max_sum_subarray(arr, k):
    max_sum = float('-infinity')
    start = 0
    curr_sum = 0
    for i, j in enumerate(arr):
        curr_sum += j
        if i - start + 1 == k: 
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
    return max_sum

arr = [2, 3, 4, 1, 5]
k = 3

print(max_sum_subarray(arr, k))