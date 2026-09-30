class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagram_dict = {}
        for string in strs:
            temp_dict = defaultdict(int)
            for char in string:
                temp_dict[char] += 1
            hashable_dict = tuple(sorted(temp_dict.items()))
            if hashable_dict in anagram_dict:
                anagram_dict[hashable_dict].append(string)
            else:
                anagram_dict[hashable_dict] = [string]
        for key in anagram_dict:
            anagrams.append(anagram_dict[key])
        return anagrams