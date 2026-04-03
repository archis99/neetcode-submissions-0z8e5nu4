class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        seen = set()

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                # if it's rotten add to q
                if grid[r][c] == 2:
                    # (r,c)
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        time = -1
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1

            time += 1

        if fresh == 0:
            return time
        else:
            return -1