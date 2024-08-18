class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        graph = [[0 for _ in range(3*n)] for _ in range(3*n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[3*i][3*j+2] = 1
                    graph[3*i+1][3*j+1] = 1
                    graph[3*i+2][3*j] = 1
                elif grid[i][j] == '\\':
                    graph[3*i][3*j] = 1
                    graph[3*i+1][3*j+1] = 1
                    graph[3*i+2][3*j+2] = 1
        visited = [[False for _ in range(3*n)] for _ in range(3*n)]
        def dfs(i, j):
            if i < 0 or i >= 3*n or j < 0 or j >= 3*n or visited[i][j] or graph[i][j]:
                return
            visited[i][j] = True
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i+x, j+y)
        regions = 0
        for i in range(3*n):
            for j in range(3*n):
                if not visited[i][j] and not graph[i][j]:
                    dfs(i, j)
                    regions += 1
        return regions