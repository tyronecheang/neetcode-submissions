class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        current_max, res = 0, 0
        while l < r:
            current_max = min(heights[l], heights[r]) * (r - l)
            res = max(current_max, res)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res