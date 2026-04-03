class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or (r,c) in visited:
                return False
            
            visited.add((r,c))

            for dr,dc in dirs:
                if dfs(r + dr,c + dc,i + 1):
                    return True
            
            visited.remove((r,c))
            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        
        return False