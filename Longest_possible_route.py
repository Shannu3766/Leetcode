class Solution:
    def longestPath(self,mat : list[list[int]],n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        len_x =len(mat)
        len_y = len(mat[0])
        max_pathcost=-1
        
        def is_valid(x,y):
            return  (0 <= x < len_x and 0 <= y < len_y and mat[x][y] == 1)
        
        def getpath(x,y,pathcost):
            nonlocal max_pathcost
            if x == xd and y ==yd:
                max_pathcost = max(pathcost, max_pathcost)
                return
            mat[x][y]=0
            dx=[0,0,-1,1]
            dy=[1,-1,0,0]
            for add_x,add_y in zip(dx,dy):
                new_x=x+add_x
                new_y=y+add_y
                if is_valid(new_x,new_y):
                    getpath(new_x,new_y,pathcost+1)
            mat[x][y]=1
            
        
        getpath(xs,ys,0)
        return max_pathcost

