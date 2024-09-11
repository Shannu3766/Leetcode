class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cols=[[] for i in range(numRows)]
        k=0
        flag=0
        if numRows==1:
            return s
        for i in range(len(s)):
            if k==numRows:
                flag=1
                k=numRows-2
            if k==0:
                flag=0
            if flag==0:
                cols[k].append(s[i])
                k=k+1
            if flag==1:
                cols[k].append(s[i])
                k=k-1
        cols=[j for i in cols for j in i]
        cols="".join(cols)
        return cols
        