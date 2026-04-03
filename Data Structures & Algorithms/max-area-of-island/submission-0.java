class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        int[][] visited = new int[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j <grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    res = Math.max(res, dfs(i, j, grid, visited));
                }
            }
        } 

        return res;
    }

    private int dfs(int r, int c, int[][] grid, int[][] visited) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length
            || grid[r][c] != 1 || visited[r][c] == 1) {
            return 0;
        }

        visited[r][c] = 1;

        return 1 + dfs(r + 1, c, grid, visited)
         + dfs(r - 1, c, grid, visited)
         + dfs(r, c + 1, grid, visited)
         + dfs(r, c - 1, grid, visited);
    }
}
