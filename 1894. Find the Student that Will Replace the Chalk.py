class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalks_left=k%sum(chalk)
        print(chalks_left)
        pos=0
        for i in range(len(chalk)):
            if chalks_left>=chalk[i]:
                chalks_left=chalks_left-chalk[i]
            else:
                return i 

        
        