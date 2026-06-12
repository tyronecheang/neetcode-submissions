class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        current_streak = 1
        max_streak = 1
        if not nums:
            return 0
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                current_streak += 1
            elif nums[i+1] == nums[i]:
                pass
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        max_streak = max(max_streak, current_streak)
        return max_streak

        