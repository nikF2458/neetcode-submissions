class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for c in strs:
            s+=str(len(c))+"#"+c
        return s
    def decode(self, strs: str) -> List[str]:
        s=[]
        i=0
        while i<len(strs):
            j=i
            while strs[j]!="#":
                j+=1
            l=int(strs[i:j])
            i=j+1
            s.append(strs[i:i+l])
            i+=l
        return s