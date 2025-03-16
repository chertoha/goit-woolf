from tree import create_test_tree


root = create_test_tree()


def count_sum(node):
    if node is None:
        return 0

    return node.val + count_sum(node.left) + count_sum(node.right)


print(count_sum(root))
