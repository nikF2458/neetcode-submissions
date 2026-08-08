class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for s in strs:
            cnt=26*[0]
            for c in s:
                cnt[ord(c)-97]+=1
            g=tuple(cnt)
            if g not in l:
                l[g]=[]
            l[g].append(s)
        return list(l.values())
