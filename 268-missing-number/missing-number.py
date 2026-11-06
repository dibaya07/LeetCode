class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        result = None
        for item in range(n+1):
            if item in nums:
                pass
            else:
                result = item
        return result