class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for num, count in count.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                if len(res) < k:
                    res.append(n)
        return res