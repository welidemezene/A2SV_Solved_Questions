# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        target = root.val
        que = deque([root])
        while que:
            curr = que.popleft()
            if curr.val != target:
                return False
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        return True        


        