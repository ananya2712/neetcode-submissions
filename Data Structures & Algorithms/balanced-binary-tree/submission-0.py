# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return [True,0]
            
            left_ht = dfs(root.left)
            right_ht = dfs(root.right)

            balanced = left_ht[0] and right_ht[0] and abs(left_ht[1] - right_ht[1]) <= 1
            return [balanced, 1+ max(left_ht[1],right_ht[1])]
            
        res = dfs(root)
        return res[0]
