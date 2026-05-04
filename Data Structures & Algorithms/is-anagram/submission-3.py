class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Compare sets of s and t
        # ??? 2 O(n)
        # return set(s) == set(t)  -- this solution does not account for 
        # count of characters

        # return ((set(s) == set(t)) and (len(s) == len(t))) --- also incorrect.
        # does not account for strings of equal length where dif letters are duplicated

        s_map = {}
        t_map = {}
        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else: 
                s_map[i] += 1

        for j in t: 
            if j not in t_map:
                t_map[j] = 1
            else: 
                t_map[j] += 1


           
        return s_map == t_map

        