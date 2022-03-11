
def visible_nodes(root):
    if not root:
     return 0

    l_sub = visible_nodes(root.left)
    r_sub = visible_nodes(root.right)
    return max(l_sub, r_sub) + 1


def visible_nodes2(root):
    return len(left_view(root))


def left_view(root):
    view = []
    queue = [root]
    while queue:
        children = []
        view.append(queue[0])
        for n in queue:
            if n.left:
                children.append(n.left)
            if n.right:
                children.append(n.right)

        queue = children

    return view
