class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        l={}
        for t in s:
            cnt=26*[0]
            for c in t:
                cnt[ord(c)-97]+=1
            g=tuple(cnt)
            if g not in l:
                l[g]=[]
            l[g].append(t)
        return list(l.values())
