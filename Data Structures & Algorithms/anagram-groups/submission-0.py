class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i: list of str
        # o: list of lists, any order

        # anagram: same chars, same number of each - cant use a set
        # can have a hashmap for each str

        # can also sort each string and compare it to other sorted strings
        # but need to preserve original order for answer

        # how to group?

        m = {}

        for index in range(len(strs)): 
            sorted_str = ''.join(sorted(strs[index]))
            if sorted_str not in m:
                m[sorted_str] = [strs[index]]
            else: 
                m[sorted_str].append(strs[index])
        return list(m.values())







        