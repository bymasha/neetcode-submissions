class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for index, value in enumerate(nums):
            compl = target - value
            if compl in nums_map:
                return [nums_map[compl], index]

            nums_map[value] = index

        return []
        
            
        