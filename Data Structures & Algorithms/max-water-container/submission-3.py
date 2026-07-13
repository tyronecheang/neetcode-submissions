class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, current_max = 0, 0
        l, r = 0, len(heights) - 1
        while l < r:
            current_max = min(heights[l], heights[r]) * (r - l)
            res = max(current_max, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res

        