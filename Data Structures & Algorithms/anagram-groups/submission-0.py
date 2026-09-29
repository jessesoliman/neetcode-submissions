class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert strings to dict
        dicts = defaultdict(list)
        for s in strs:
            string_dict = [0] * 26
            for char in s:
                string_dict[ord(char)-97] += 1
            dicts[tuple(string_dict)].append(s)
        return list(dicts.values())
            
                