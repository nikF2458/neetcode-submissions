class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=26*[0]
        for n in range(len(s)):
            c[ord(s[n])-97]+=1
            if len(s)==len(t):
                c[ord(t[n])-97]-=1
        for n in c:
            if n!=0:
                return False
        return True
