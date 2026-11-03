class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_sets = set(nums)
        if len(nums) != len(my_sets):
            return True
        else:
            return False
