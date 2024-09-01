class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        coordinates=[coordinate1,coordinate2]
        colors=["black","black"]
        x_vals=['a','c','e','g']
        p=0
        for i in coordinates:
            if i[0] in x_vals:
                if int(i[1])%2==0:
                    colors[p]="white"
            else:
                if int(i[1])%2!=0:
                    colors[p]="white"
            p+=1
        if colors[0]==colors[1]:
            return True
        else:
            return False
        