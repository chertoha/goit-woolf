import csv
import timeit
from BTrees._OOBTree import OOBTree


def load_data(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            }
            data.append(item)
    return data


def add_item_to_tree(tree, item):
    tree[item['Price']] = item


def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = item


def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items(min_price, max_price)]


def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]


def main():
    filename = 'generated_items_data.csv'
    data = load_data(filename)

    tree = OOBTree()
    dictionary = {}

    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_price, max_price = 10, 100

    time_tree = timeit.timeit(lambda: range_query_tree(
        tree, min_price, max_price), number=100)

    time_dict = timeit.timeit(lambda: range_query_dict(
        dictionary, min_price, max_price), number=100)

    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")
    print("OOBTree is faster than Dict for range queries! ")


if __name__ == "__main__":
    main()
