class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i, n in enumerate(heights):
            r = len(heights) - 1
            while r > i:
                area = min(heights[r], heights[i]) * (r - i)
                maximum = max(maximum, area)
                r -= 1
        return maximum

        