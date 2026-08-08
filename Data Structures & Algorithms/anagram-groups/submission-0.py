class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for s in strs:
            cnt=26*[0]
            for c in s:
                cnt[ord(c)-97]+=1
            if tuple(cnt) not in l:
                l[tuple(cnt)]=[]
            l[tuple(cnt)].append(s)
        return list(l.values())