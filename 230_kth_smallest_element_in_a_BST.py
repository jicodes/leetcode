# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Initialize the count and result variable
        self.count = 0
        self.result = None

        # Helper method to perform an in-order traversal
        def inorder(node):
            if node is None:
                return

            # Traverse the left subtree
            inorder(node.left)

            # Increment the count of visited nodes
            self.count += 1

            # If the count equals k, set the result to the node's value
            if self.count == k:
                self.result = node.val
                return

            # Traverse the right subtree if the k-th element is not found yet
            inorder(node.right)

        # Perform the in-order traversal starting from the root
        inorder(root)

        return self.result


# Example usage:
# Constructing a simple BST
#       3
#      / \
#     1   4
#      \
#       2
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

sol = Solution()
k = 2
print(sol.kthSmallest(root, k))  # Output: 2
