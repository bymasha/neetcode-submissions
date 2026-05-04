class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i: list of str
        # o: list of lists, any order

        # anagram: same chars, same number of each - cant use a set
        # can have a hashmap for each str

        # can also sort each string and compare it to other sorted strings
        # but need to preserve original order for answer

        # how to group?

        # m = {}
        m = defaultdict(list)


        for string in strs: 
            sorted_str = ''.join(sorted(string))
            # if sorted_str not in m:
            #     m[sorted_str] = [string]
            # else: 
            m[sorted_str].append(string)
        return list(m.values())







        