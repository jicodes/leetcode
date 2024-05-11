# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for the Solution class
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca and right_lca:
            return root
        elif left_lca:
            return left_lca
        else:
            return right_lca


# Test case
def test_lowestCommonAncestor():
    # Constructing a binary tree
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    solution = Solution()

    # Test case 1: p = 5, q = 1
    p = root.left
    q = root.right
    assert solution.lowestCommonAncestor(root, p, q).val == 3

    # Test case 2: p = 5, q = 4
    p = root.left
    q = root.left.right.right
    assert solution.lowestCommonAncestor(root, p, q).val == 5

    print("All test cases passed!")


# Run the test cases
test_lowestCommonAncestor()
