class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or curr_sum > target:
                return

            subset.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])

            subset.pop()
            # escape all the equal numbers
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_sum)

        dfs(0, 0)
        return res