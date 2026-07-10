class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        current_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            current_max = (r - l) * min(heights[l], heights[r])
            maximum = max(maximum, current_max)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
        return maximum
        