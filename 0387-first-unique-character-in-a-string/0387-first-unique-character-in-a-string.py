class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen ={}
        for i in s:
            seen[i]= seen.get(i,0)+1
        for j in range(len(s)):
            if seen[s[j]] ==1:
                return j
        return -1