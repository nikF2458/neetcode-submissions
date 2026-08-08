class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = [0] * 26

        for n in range(len(s)):
            cnt[ord(s[n]) - 97] += 1
            cnt[ord(t[n]) - 97] -= 1
        
        for n in cnt:
            if n != 0:
                return False
        
        return True