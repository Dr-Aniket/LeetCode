class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = [''.join(sorted(i)) for i in strs]
        
        grps = {}

        for i in range(len(strs)):
            if lst[i] in grps:
                grps[lst[i]].append(i)
            else:
                grps[lst[i]] = [i]

        return [[strs[i] for i in grps[lst]] for lst in grps]
