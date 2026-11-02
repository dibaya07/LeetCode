class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        final_ans=[]
        seen = {}
        for i, item in enumerate(nums):
            amount = target - item
            if amount in seen:
                final_ans += [seen[amount],i]
                break
            seen[item] = i
            if len(final_ans) > 0:
                break
        return final_ans    