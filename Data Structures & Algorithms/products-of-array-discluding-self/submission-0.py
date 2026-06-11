class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            product = 1
            for j, k in enumerate(nums):
                if j != i:
                    product *= k
            res.append(product)
        return res
        