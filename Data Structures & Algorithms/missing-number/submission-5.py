class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        needed_sum = (1 + n)/2 * n
        nums_sum = sum(nums)

        return int(needed_sum - nums_sum)




       
        



        

        


     
        