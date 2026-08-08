class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c=26*[0]
        for n in range(len(s)):
            c[ord(s[n])-97]+=1
            c[ord(t[n])-97]-=1
        for n in c:
            if n!=0:
                return False
        return True