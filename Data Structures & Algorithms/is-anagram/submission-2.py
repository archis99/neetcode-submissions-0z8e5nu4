class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(count)):
            if count[i] != 0:
                return False

        # sDict = defaultdict(int)
        # tDict = defaultdict(int)

        # for ch in s:
        #     sDict[ch] += 1
        
        # for ch in t:
        #     tDict[ch] += 1

        # for ch in sDict:
        #     if sDict[ch] != tDict[ch]:
        #         return False
        return True