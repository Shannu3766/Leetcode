class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sums=sum(rolls)
        required_sum=(mean*(len(rolls)+n))-sum(rolls)
        if required_sum//n<1 or required_sum//n>6:
            return []
        p=[required_sum//n ]*n
        left_val=required_sum%n
        while left_val!=0:
            for i in range(n):
                if left_val==0:
                    break
                p[i]+=1
                if p[i]>6 or p[i]<0:
                    return []
                left_val-=1
        return p