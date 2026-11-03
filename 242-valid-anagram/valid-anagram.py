class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for item1 in s:
            if s.count(item1) == t.count(item1):
                pass
            else:
                return False
        return True