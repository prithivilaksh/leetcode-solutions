# Problem: Count Subarrays With At Least K Pairs

# You are given an array of integers nums and an integer k.

# A pair means two identical numbers in the same subarray.
# For example:

# [1,1,2] has 1 pair (the two 1s).

# [1,1,1] also has 1 pair, because only two of the 1s can form a pair.

# [2,2,2,2] has 2 pairs, since 4 copies of 2 can be grouped into 2 pairs.

# Your task is to count how many subarrays of nums contain at least k pairs.


# Examples

# Example 1
# Input: nums = [1,2,3,1,2], k = 2
# Output: 1
# Explanation: Only the full subarray [1,2,3,1,2] has 2 pairs (1s form one pair, 2s form another).

# Example 2
# Input: nums = [1,1,3,1,1], k = 2
# Output: 1
# Explanation: The entire array has 2 pairs (4 ones → 2 pairs).

# Example 3
# Input: nums = [1,1,1,2,2], k = 2
# Output: 2
# Explanation: The subarrays [1,1,2,2] and [1,1,1,2,2] each have 2 pairs.
from collections import defaultdict

def solution(fruits, k):
    n = len(fruits)
    cnt = defaultdict(int)
    pairs = 0
    res = 0
    left = 0

    for right in range(n):
        # Add new element
        cnt[fruits[right]] += 1
        if cnt[fruits[right]] % 2 == 0:  # new pair formed
            pairs += 1

        # Shrink window while we have at least k pairs
        while pairs >= k:
            res += n - right  # all subarrays starting at left are valid
            # Remove left element
            if cnt[fruits[left]] % 2 == 0:  # breaking a pair
                pairs -= 1
            cnt[fruits[left]] -= 1
            left += 1

    return res