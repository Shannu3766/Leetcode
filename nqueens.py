class Solution:
    def nQueen(self, n):
        paths=[]
        
        def ismovevalid(path,x,y):
            for path_x,path_y in path:
                if path_x == x or path_y == y or abs(path_x-x)==abs(path_y-y):
                    return False
            return True
        
        def get_path(depth,path):
            nonlocal paths
            if depth == n-1:
                print(path)
                paths.append(path)
            for i in range(n):
                new_path = path + [[depth+1,i]]
                if ismovevalid(path,depth+1,i):
                    # print(new_path)
                    get_path(depth+1,new_path)
        
        for i in range(n):
            get_path(0,[[0,i]])
        
        ans=[]
        for path in paths:
            out=[]
            for x,y in  path:
                out.append(y+1)
            ans.append(out)
        print(ans)
A=Solution()
A.nQueen(4)