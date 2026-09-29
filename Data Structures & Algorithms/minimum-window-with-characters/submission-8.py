class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l, r = 0, 0
        t_dict = Counter(t)
        s_dict = {key: 0 for key in t_dict}
        s_over = {key: 0 for key in t_dict}
        
        
        while r < len(s) and l < len(s) - len(t) + 1:
            # move to valid chars
            while s[l] not in t_dict:
                l += 1
                if l >= len(s) - len(t) + 1:
                    break
            while s[r] not in t_dict:
                r += 1
                if r >= len(s):
                    break
            # add valid r char
            if r < len(s):
                if s_dict[s[r]] == t_dict[s[r]]:
                    s_over[s[r]] += 1
                else:
                    s_dict[s[r]] += 1
            # move r and continue loop if dicts not equal
            if s_dict != t_dict:
                r += 1
                continue
            # if dicts equal, evaulate res and move l until dicts not equal
            while s_dict == t_dict:
                if res != "":
                    res = min(res, s[l:r+1], key=len)
                else:
                    res = s[l:r+1]
                if s[l] in t_dict:
                    if s_over[s[l]] > 0:
                        s_over[s[l]] -= 1
                    else:
                        s_dict[s[l]] -= 1
                l += 1
            r += 1
        return(res)
            