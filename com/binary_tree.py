import math


class Node:
    """
    Node class: represents basic node class that Tree data structure will depend on to represent its children nodes
    """
    def __init__(self, value, left_child=None, right_child=None, upper_limit=None, lower_limit=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str("Node (" + str(self.value) + ")")


class Tree:
    """
    Tree class: Represents Tree class that Tree data structure
    """
    def __init__(self, root):
        self.root = root
        self.current = root
        self.parent = None
        self.left_height = 0
        self.right_height = 0

    def insert(self, value):
        self.find(value, reset=True)
        if value < self.parent.value:
            self.parent.left_child = Node(value)
        elif value > self.parent.value:
            self.parent.right_child = Node(value)

    def find(self, value, reset: bool = False):
        if reset:
            self.current = self.root
        if self.current:
            if value == self.current.value:
                return self.current
            elif value < self.current.value:
                self.parent = self.current
                self.current = self.current.left_child

            elif value > self.current.value:
                self.parent = self.current
                self.current = self.current.right_child
            return self.find(value)

    def depth_first_pre_order(self, node: Node):
        if node:
            print(node.value)
            if node.left_child:
                if node.left_child:
                    self.depth_first_pre_order(node.left_child)
            if node.right_child:
                if node.right_child:
                    self.depth_first_pre_order(node.right_child)

    def depth_first_in_order(self, node: Node):
        if node:
            if node.left_child:
                self.depth_first_in_order(node.left_child)
            print(node.value)
            if node.right_child:
                self.depth_first_in_order(node.right_child)

    def depth_first_post_order(self, node: Node):
        if node:
            if node.left_child:
                self.depth_first_post_order(node.left_child)
            if node.right_child:
                self.depth_first_post_order(node.right_child)
            print(node.value)

    def get_height(self, node: Node):
        if node is None:
            return -1
        return 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

    def get_minimum(self, node: Node):
        if node:
            if node.left_child is None and node.right_child is None:
                return node.value
            if node.left_child and node.right_child:
                return min(node.value, self.get_minimum(node.left_child), self.get_minimum(node.right_child))
            if node.left_child and node.right_child is None:
                return min(node.value, self.get_minimum(node.left_child))
            if node.right_child and node.left_child is None:
                return min(node.value, self.get_minimum(node.right_child))

    def equals(self, t: 'Tree' = None):
        if self.root.value != t.root.value:
            return False
        return self.__equals(self.root, t.root)

    def __equals(self, first_node: Node, second_node: Node):
        if first_node and second_node:
            return (first_node.value == second_node.value and self.__equals(
                first_node.left_child, second_node.left_child) and
                    self.__equals(first_node.right_child, second_node.right_child))
        if (first_node and second_node is None) or (first_node is None and second_node):
            return False
        if first_node is None and second_node is None:
            return True

    def is_bst(self):
        return self.__is_bst(self.root, -math.inf, math.inf)

    def __is_bst(self, node: Node, min_value, max_value):
        if node is None:
            return True
        result = min_value <= node.value <= max_value and self.__is_bst(
            node.left_child, min_value, node.value - 1) and self.__is_bst(
            node.right_child, node.value + 1, max_value)
        print(f"Result: {result} for node {node.value} with min value {min_value} and max value {max_value}")
        return result

    def get_nodes_at_distance(self, distance: int):
        self.__get_nodes_distance(self.root, distance)

    def __get_nodes_distance(self, node: Node, distance: int):
        if node is None:
            return "No nodes found"
        if distance == 0:
            print(f"{node.value}, ")
        self.__get_nodes_distance(node.left_child, distance - 1)
        self.__get_nodes_distance(node.right_child, distance - 1)

    def breadth_first_search(self):
        distance = self.get_height(self.root)
        i = 0
        while i <= distance:
            self.__get_nodes_distance(self.root, i)
            i += 1

    def __breadth_first_search(self, node: Node):
        if node is None:
            return
        print(f"{node.value}, ")
        self.__breadth_first_search(node.left_child)


if __name__ == '__main__':
    first_tree = Tree(Node(20, left_child=Node(10, left_child=Node(6, left_child=Node(3), right_child=Node(8)),
                                               right_child=Node(21)), right_child=Node(30, left_child=Node(4))))
    second_tree = Tree(Node(20, left_child=Node(10, left_child=Node(6, left_child=Node(3), right_child=Node(8)),
                                                right_child=Node(21)), right_child=Node(30, left_child=Node(4))))
    # print(tree.find(5, reset=True).value)
    # print(tree.find(10, reset=True).value)
    # print(tree.find(12, reset=True).value)
    # print(tree.find(20, reset=True).value)
    # tree.insert(1)
    # print(tree.find(11, reset=True).value)
    # tree.insert(19)
    # tree.insert(9)
    # print('Depth First Traversal In Order')
    # tree.depth_first_in_order(tree.root)
    # print('Depth First Traversal Pre Order')
    # tree.depth_first_pre_order(tree.root)
    # print('Depth First Traversal Post Order')
    # tree.depth_first_post_order(tree.root)
    # print(tree.get_height(tree.root))
    # print(tree.get_minimum(tree.root))
    # print(first_tree.equals(second_tree))
    # print(f"is bst : {first_tree.is_bst()}")
    # first_tree.get_nodes_at_distance(0)
    # first_tree.breadth_first_search()
