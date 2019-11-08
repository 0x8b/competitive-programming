def height(root):
    l = 1 + height(root.left) if root.left else 0
    r = 1 + height(root.right) if root.right else 0

    return max(l, r)
