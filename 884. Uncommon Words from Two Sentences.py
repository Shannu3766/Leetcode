class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        vals={}
        for i in s1:
            if i in vals:
                vals[i]+=1
            else:
                vals[i]=1
        for i in s2:
            if i in vals:
                vals[i]+=1
            else:
                vals[i]=1
        out=[]
        for i in vals:
            if vals[i]==1:
                out.append(i)
        return out
        