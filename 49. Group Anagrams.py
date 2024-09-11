class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals={}
        for i in strs:
            p="".join(sorted(list(i)))
            if p in vals:
                vals[p].append(i)
            else:
                vals[p]=[i]
        output=[]
        for i in vals:
            output.append(sorted(vals[i]))
        return output
        