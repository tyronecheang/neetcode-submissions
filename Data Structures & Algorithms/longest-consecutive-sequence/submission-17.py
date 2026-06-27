class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current_max, res = 1, 0
        nums_set = set(nums)

        for n in nums:
            if n - 1 not in nums_set:
                current_max = 1
                while n + current_max in nums_set:
                    current_max += 1
            
            res = max(current_max, res)
        return res
        