# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def symmetry(self, left, right):
        if left == None and right == None:
            return True
        if left == None and right != None or right == None and left != None:
            return False
        if left.val != right.val:
            return False
        return self.symmetry(left.left, right.right) and self.symmetry(left.right, right.left)

    def isSymmetric(self, root):
        if root == None:
            return True
        return self.symmetry(root.left, root.right)
        """
        :type root: TreeNode
        :rtype: bool
        """
