class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(num == 0 for num in nums): return 0
        x = 0
        for num in nums: x ^= num
        return len(nums) if x != 0 else len(nums) - 1