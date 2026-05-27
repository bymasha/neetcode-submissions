class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # get [0], [-1] from nums
        # create default dict
        # for num in range( , ) if num not in dict return num
        from collections import defaultdict


        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        for e in range(len(nums) + 1):
            if e not in d:
                return e 

        return 0

            



        