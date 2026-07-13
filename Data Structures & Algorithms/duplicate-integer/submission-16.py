class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = []
        for n in nums:
            if n in has_seen:
                return True
            has_seen.append(n)
        return False
        