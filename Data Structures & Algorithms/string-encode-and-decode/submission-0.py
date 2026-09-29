class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "#" + string
        return encoded_str


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            size = str()
            while s[i] != '#':
                size += s[i]
                i += 1
            i += 1
            size = int(size)
            word = str()
            for j in range(size):
                word += s[i]
                i += 1
            res.append(word)
        return res
