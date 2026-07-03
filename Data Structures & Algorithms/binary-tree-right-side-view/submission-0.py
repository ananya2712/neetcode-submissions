# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:     
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do level order traversal and print the lestmost node
        res = []

        def dfs(curr, depth):
            if curr is None:
                return None
            
            if len(res) == depth:
                res.append([])

            res[depth].append(curr.val)
            if curr.left:
                dfs(curr.left, depth + 1)
            if curr.right:
                dfs(curr.right, depth +1)
            
        dfs(root,0)
        final = []
        for l in res:
            final.append(l[-1])
        return final