class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        for num, count in count_map.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                if len(res) < k:
                    res.append(n)
        return res


        