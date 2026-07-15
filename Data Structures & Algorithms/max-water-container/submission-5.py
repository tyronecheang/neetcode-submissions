class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentmax, res = 0, 0
        l, r = 0, len(heights) - 1
        while l < r:
            current_max = min(heights[l], heights[r]) * (r - l)
            res = max(res, current_max)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res
        