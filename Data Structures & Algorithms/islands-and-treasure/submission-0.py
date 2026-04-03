class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # (r,c,distance)
                    q.append((r, c, 0))
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            print(q)
            r, c, dist = q.popleft()

            for dr, dc in dirs:
                if (r + dr) >= rows or (r + dr) < 0 or (c + dc) >= cols or (c + dc) < 0 or grid[r + dr][c + dc] != 2147483647:
                    continue
                
                grid[r + dr][c + dc] = dist + 1
                q.append((r + dr, c + dc, dist + 1))
