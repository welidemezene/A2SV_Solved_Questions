
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.val != root.val:
                return False
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)    
        return True