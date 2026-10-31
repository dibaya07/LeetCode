class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        previous_idx = []
        final_ans = []
        for item1 in range(len(nums)):
            if target > 0:
                second_value = abs(target - nums[item1]) 
                if second_value in nums and nums.index(second_value) != item1:
                    if nums[item1] + second_value == target:
                        print("step1")
                        final_ans += [item1, nums.index(second_value)]
                        break
            for item2 in range(len(nums)):
                if item1 == item2 or item2 in previous_idx:
                    pass
                else:
                    if target > 0:
                        second_value = abs(target - nums[item2])
                        if second_value in nums and nums.index(second_value) != item2:
                            print("step2")
                            if second_value + nums[item2] == target:
                                final_ans += [item2, nums.index(second_value)]
                                break
                    else:
                        if nums[item1] + nums[item2] == target:
                            print("step3")
                            final_ans += [item1, item2]
                            break
            previous_idx.append(item1)
            if len(final_ans) > 0:
                break
        return final_ans