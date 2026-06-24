class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = [[] for _ in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for num, count in count.items():
            occurences[count].append(num)
        
        res = []
        for i in range(len(occurences) -1, -1, -1):
            for n in occurences[i]:
                if len(res) < k:
                    res.append(n)
        return res