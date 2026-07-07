class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = set()

        for n in nums:
            if n in has_seen:
                return True
            has_seen.add(n)
        return False