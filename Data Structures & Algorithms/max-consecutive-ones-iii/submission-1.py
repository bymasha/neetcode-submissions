class Solution:
    #  [1, 1, 1] k = 2
    def longestOnes(self, nums: List[int], k: int) -> int:
        r = 0 
        max_length = 0
        counter = 0

        for l in range(len(nums)):
            while r < len(nums): 
                if nums[r] == 0:
                    if counter + 1 <= k: 
                        counter += 1
                    else:
                        break

                r += 1
            len_arr = r - l
            max_length = max(max_length, len_arr)
                
            if nums[l] == 0:
                counter -= 1
        return max_length

                









        