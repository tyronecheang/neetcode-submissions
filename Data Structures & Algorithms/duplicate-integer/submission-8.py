class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = []

        for n in nums:
            if n in nums_list:
                return True
            nums_list.append(n)

        return False 

        