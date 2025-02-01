import csv
import timeit
from BTrees.OOBTree import OOBTree


def load_data(filename):
    items = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["ID"] = int(row["ID"])
            row["Price"] = float(row["Price"])
            items.append(row)
    return items


def add_item_to_tree(tree, item):
    tree[item["ID"]] = item


def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item


def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]


def range_query_dict(dictionary, min_price, max_price):
    return [
        item for item in dictionary.values() if min_price <= item["Price"] <= max_price
    ]


def benchmark_range_query(structure, query_function, min_price, max_price, runs=100):
    return timeit.timeit(
        lambda: query_function(structure, min_price, max_price), number=runs
    )


filename = "items_data.csv"
data = load_data(filename)

oob_tree = OOBTree()
dict_store = {}

for item in data:
    add_item_to_tree(oob_tree, item)
    add_item_to_dict(dict_store, item)


min_price, max_price = 10.0, 50.0

oobtree_time = benchmark_range_query(oob_tree, range_query_tree, min_price, max_price)
dict_time = benchmark_range_query(dict_store, range_query_dict, min_price, max_price)


print(f"Total range_query time for OOBTree: {oobtree_time:.3f} seconds")
print(f"Total range_query time for Dict: {dict_time:.3f} seconds")
