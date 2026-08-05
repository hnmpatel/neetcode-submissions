class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)].append(s)
        return list(anagrams.values())

    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams.keys():
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        return [v for v in anagrams.values()]
        