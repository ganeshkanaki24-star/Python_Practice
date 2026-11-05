# 40. Find the lowest common ancestor of two nodes in a binary tree.

def lowest_common_ancestor(root, p, q):

    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)

    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root

    if left is not None:
        return left

    return right


# Create a binary tree

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = lowest_common_ancestor(root, 4, 5)

if result is not None:
    print("Lowest Common Ancestor:", result.val)
else:
    print("Ancestor not found")