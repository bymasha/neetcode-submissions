class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # get [0], [-1] from nums
        # create default dict
        # for num in range( , ) if num not in dict return num

        return (set(range(len(nums) + 1)) - set(nums)).pop()


            



        