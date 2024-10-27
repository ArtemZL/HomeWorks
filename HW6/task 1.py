class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

def build_tree():
    root = Node(1, int(input("Введіть значення кореня: ")))
    nodes = {1: root}

    while True:
        try:
            parent_id = int(input("Введіть ID батьківської вершини (0 для завершення): "))
            if parent_id == 0:
                break

            child_id = int(input("Введіть ID нової вершини: "))
            child_value = int(input("Введіть значення нової вершини: "))
            position = input("Ліва чи права вершина? (left/right): ").strip().lower()

            if parent_id in nodes:
                child_node = Node(child_id, child_value)
                nodes[child_id] = child_node
                if position == "left":
                    nodes[parent_id].add_left(child_node)
                elif position == "right":
                    nodes[parent_id].add_right(child_node)
            else:
                print("Батьківська вершина не знайдена.")

        except ValueError:
            print("Невірні дані, спробуйте ще раз.")

    return root

def max_sum_path(node):
    if not node:
        return (0, [])

    left_sum, left_path = max_sum_path(node.left)
    right_sum, right_path = max_sum_path(node.right)

    if left_sum > right_sum:
        return (left_sum + node.value, [node.id] + left_path)
    else:
        return (right_sum + node.value, [node.id] + right_path)

root = build_tree()
max_sum, path = max_sum_path(root)
print(f"Максимальна сума шляху: {max_sum}")
print(f"Шлях від кореня до листка: {' -> '.join(map(str, path))}")
