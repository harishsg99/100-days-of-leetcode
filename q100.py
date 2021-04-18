class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return True 
  
        if p is not None and q is not None:
            return ((p.val == q.val) and self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
      
        return False
