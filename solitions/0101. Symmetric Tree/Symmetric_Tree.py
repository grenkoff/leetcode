# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_stack = [root.left]
        right_stack = [root.right]

        right_visited = []
        left_visited = []

        while len(left_stack) != 0:
            curr = left_stack.pop()
            if curr:
                left_visited.append(curr.val)
                left_stack.append(curr.right)
                left_stack.append(curr.left)
            else:
                left_visited.append(None)

        while len(right_stack) != 0:
            curr = right_stack.pop()
            if curr:
                right_visited.append(curr.val)
                right_stack.append(curr.left)
                right_stack.append(curr.right)
            else:
                right_visited.append(None)

        return left_visited == right_visited
    
    # Recursive Solution
    def checkOpposite(self,lRoot,rRoot):
        if rRoot == None and lRoot == None:
            return True
        if (rRoot and lRoot )== None:
            return False
        
        if rRoot.val == lRoot.val:
            return self.checkOpposite(lRoot.left, rRoot.right) and self.checkOpposite(lRoot.right,rRoot.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None or (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        lRoot = root.left
        rRoot = root.right

        return self.checkOpposite(lRoot,rRoot)
