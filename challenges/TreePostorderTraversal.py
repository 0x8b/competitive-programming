def postOrder(root):
    if root.left:
        postOrder(root.left)

    if root.right:
        postOrder(root.right)

    print(root, end = " ")
