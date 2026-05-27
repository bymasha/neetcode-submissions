class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # get [0], [-1] from nums
        # create default dict
        # for num in range( , ) if num not in dict return num

        for e in range(len(nums) + 1):
            if e not in nums:
                return e 


            



        