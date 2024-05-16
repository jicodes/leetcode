from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: If either preorder or inorder is empty, return None
        if not preorder or not inorder:
            return None

        # Root of the current subtree is the first element of preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of root_val in inorder traversal
        root_index_inorder = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(
            preorder[1 : 1 + root_index_inorder], inorder[:root_index_inorder]
        )
        root.right = self.buildTree(
            preorder[1 + root_index_inorder :], inorder[root_index_inorder + 1 :]
        )

        return root
