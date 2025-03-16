from tree import create_test_tree


root = create_test_tree()


def find_max(node):
    if node.right is None:
        return node.val

    return find_max(node.right)


print(find_max(root))
