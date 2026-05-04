class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sorted in an non inc order >>> could be duplicates
        # also means whatever is on thw sides is either big or small
        # includes negative numbers 
        # after squaring > order changes

        # for loop > O(n), sort O(nlog n)

        # we can build the array in an oppsite order an then reverse, which is a O(n) operation unlike sorting

        l = 0 
        r = len(nums) - 1
        res = []

        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[r]**2)
                r -= 1
            else: 
                res.append(nums[l]**2)
                l += 1

        return res[::-1]








        