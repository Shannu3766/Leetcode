maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
length=len(maze)
breadth=len(maze[0])
def is_valid(x,y):
    if 0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y]==1:
        return True
    return False

def get_route(x,y,word,path):
    if x==length-1 and y==breadth-1:
        print(word)
        return
    maze[x][y]=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    direction=["L","R","D","U"]
    for index,direct in enumerate(direction):
        new_x = x+dx[index]
        new_y = y+dy[index]
        new_path = path + [[new_x,new_y]]
        if is_valid(new_x,new_y):
            get_route(new_x,new_y,word=word+direct,path=new_path)
    maze[x][y]=1
get_route(0,0,"",[[0,0]])