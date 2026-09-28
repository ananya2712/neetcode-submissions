class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # DF with default type as list
        res = defaultdict(list)

        for s in strs:
            # sort string characters
            sorted_strings = ''.join(sorted(s))

            # add to group based on sorted key
            res[sorted_strings].append(s)

        return list(res.values())