class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = []
        for index, value in enumerate(nums):
            nums_map.append([value, index])
            # does order matter

        nums_map.sort()
        # how does sort work for list of lists
        l = 0 
        r = len(nums) - 1

        # while l != r: # this does not allow for equality but allows for crossing
        while l < r : 
            res_sum = nums_map[l][0] + nums_map[r][0] 
            if res_sum == target:
                return [min(nums_map[l][1], nums_map[r][1]),
                        max(nums_map[l][1], nums_map[r][1])]
            elif res_sum < target: 
                l += 1
            else: 
                r -= 1
        return []







        