class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set, res = set(nums), 0

        current_max = 1
        for n in nums_set:
            if n - 1 not in nums_set:
                current_max = 1
            
                while n + current_max in nums_set:
                    current_max += 1
            
            res = max(res, current_max)
        return res

        