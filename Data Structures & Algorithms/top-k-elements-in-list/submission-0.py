class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} # hash map which holds value : frequency
        for n in nums: # for loop iterates through nums list
            freq_map[n] = freq_map.get(n, 0) + 1 # add frequency upon appearance

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]