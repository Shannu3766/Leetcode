class Solution:
    def dectobin(self,num):
        p=""
        while num>0:
            if num%2==0:
                p+="0"
            else:
                p+="1"
            num=int(num/2)
        p=p[::-1]
        return p

    def minBitFlips(self, start: int, goal: int) -> int:
        start=self.dectobin(start)
        goal=self.dectobin(goal)
        if len(start)!=len(goal):
            if len(start)<len(goal):
                val=len(goal)-len(start)
                for i in range(val):
                    start="0"+start
            else:
                val=len(start)-len(goal)
                for i in range(val):
                    goal="0"+goal
        vount=0
        for i in range(len(goal)):
            if goal[i]!=start[i]:
                vount+=1
        return vount