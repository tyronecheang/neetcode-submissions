class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            c = ''.join(sorted(s))
            if c in anagram_map:
                anagram_map[c].append(s)
            if c not in anagram_map:
                anagram_map[c] = []
                anagram_map[c].append(s)
        return list(anagram_map.values())