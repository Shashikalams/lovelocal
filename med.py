class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root

def build_tree(lst, idx=0):
    if idx < len(lst) and lst[idx] is not None:
        node = TreeNode(lst[idx])
        node.left = build_tree(lst, 2 * idx + 1)
        node.right = build_tree(lst, 2 * idx + 2)
        return node
    return None


def convert_to_list(input_str):
    return [None if x == 'null' else int(x) for x in input_str.split(',')]

input_list = input("root=")
tree_list = convert_to_list(input_list)
root = build_tree(tree_list)

p_val = int(input("p="))
q_val = int(input("q="))
p = TreeNode(p_val)
q = TreeNode(q_val)

lca = lowest_common_ancestor(root, p, q)
print(f"The LCA of nodes {p.val} and {q.val} is {lca.val}")
