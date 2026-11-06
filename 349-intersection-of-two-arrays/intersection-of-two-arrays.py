class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for item in nums2:
            if item in nums1 and item not in result:
                result.append(item)
            else:
                pass
        return result