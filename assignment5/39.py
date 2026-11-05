# 39. Serialize and deserialize a binary tree.

class TreeNode:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def serialize(root):

    values = []

    def preorder(node):

        if node is None:
            values.append("None")
            return

        values.append(str(node.val))

        preorder(node.left)
        preorder(node.right)

    preorder(root)

    return ",".join(values)


def deserialize(data):

    values = iter(data.split(","))

    def build_tree():

        value = next(values)

        if value == "None":
            return None

        node = TreeNode(int(value))

        node.left = build_tree()
        node.right = build_tree()

        return node

    return build_tree()


# Create a binary tree

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

data = serialize(root)

print("Serialized Tree:", data)

new_root = deserialize(data)

print("Deserialized Root:", new_root.val)