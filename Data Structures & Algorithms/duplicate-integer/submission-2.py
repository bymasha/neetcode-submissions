class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap
        # 1. If we reach count >1 > return 
            # Worst case T: O(n) S: O(n)
        # 2. Finish the map and check all values
            # For sure O(n) because we will have to go through entire list

        count_map = {}

        for num in nums: 
            if num in count_map:
                return True
            count_map[num] = 1
        return False

