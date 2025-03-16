from tree import create_test_tree


root = create_test_tree()


def find_min(node):
    if node.left is None:
        return node.val

    return find_min(node.left)


print(find_min(root))
