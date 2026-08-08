class Solution:
    def hasDuplicate(self, x: List[int]) -> bool:
        dup = set()
        for n in x:
            if n in dup:
                return True
            dup.add(n)
        return False