class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, data):
        self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = TreeNode(data)
            else:
                self._insert_recursive(current.right, data)

    def visualize(self):
        self._visualize_recursive(self.root, 0)

    def _visualize_recursive(self, current, depth):
        if current:
            # (reverse inorder traversal)
            self._visualize_recursive(current.right, depth + 1)
            
           
            print("-" * depth, current.data)
            
            # Print the left subtree
            self._visualize_recursive(current.left, depth + 1)


if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(105)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(20)

    tree.visualize()
