def inOrder(root):
    if root.left:
        inOrder(root.left)

    print(root, end=" ")

    if root.right:
        inOrder(root.right)
