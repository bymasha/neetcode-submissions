class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Go by element of nums and compare a sum of that element and next 
        # to target
        # as soon as == target, return sorted()

        # first tries to start from 1 

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res = [i,j]
                    return sorted(res)
