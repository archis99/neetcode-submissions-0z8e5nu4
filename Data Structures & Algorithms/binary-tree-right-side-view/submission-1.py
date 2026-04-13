# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root)])
        res = []

        while q:
            qlen = len(q)
            right = -1
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    right = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            # if right is not collected, then don't append it
            if right != -1:
                res.append(right)


        return res