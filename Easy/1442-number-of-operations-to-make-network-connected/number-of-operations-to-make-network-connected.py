class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<(n-1):
            return -1
        graph = defaultdict(list)
        for _from,_to in connections:
            graph[_from].append(_to)
            graph[_to].append(_from)


        def dfs(node):
            visited.add(node)
            for connection in graph[node]:
                if connection not in visited:
                    dfs(connection)
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count-1
            



        