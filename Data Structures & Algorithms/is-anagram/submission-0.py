class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        oneS, oneT = {}, {}

        for i in range(len(s)):
            oneS[s[i]] = 1 + oneS.get(s[i], 0)
            oneT[t[i]] = 1 + oneT.get(t[i], 0)
        return oneS == oneT

