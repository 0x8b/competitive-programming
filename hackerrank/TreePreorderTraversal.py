def preOrder(root):
    print(root, end = " ")

    if root.left:
        preOrder(root.left)

    if root.right:
        preOrder(root.right)
