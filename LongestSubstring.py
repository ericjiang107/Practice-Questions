'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

def longSubString(String, K):
    count = 0
    window_start = 0
    alist = list(String)
    empty_dic = {}
    for letter in range(len(alist)):
        if letter not in empty_dic:
            empty_dic[alist[letter]] = 1
        else:
            empty_dic[alist[letter]] += 1
        while len(empty_dic) > K:
            if empty_dic[alist[letter]] == 1:
                del empty_dic[alist[letter]]
            else:
                empty_dic[alist[letter]] -= 1
            window_start += 1
        if len(empty_dic) == K:
            count = max(count, sum(empty_dic.values()))
    return count

print(longSubString("araaci", 2))