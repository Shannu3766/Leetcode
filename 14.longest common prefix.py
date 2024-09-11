class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        flag=0
        for i in range(len(strs[0])+1):
            pre=[x[:i] for x in strs]
            for k in range(len(pre)-1):
                if pre[k]!=pre[k+1]:
                    flag=1
                    break
            if flag==1:
                break
            ans=pre[0][:i]
        return ans