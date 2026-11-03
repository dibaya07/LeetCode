class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen={}
        for i, item in enumerate(nums):
            if item in seen:
                return True
            else:
                seen[item]=i
        return False
    