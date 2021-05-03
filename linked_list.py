class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


def delete_node(head, index):
    if index == 0:
        return head.next
    previous_node = get_node_by_index(head, index - 1)
    next_node = get_node_by_index(head, index + 1)
    previous_node.next = next_node
    return head


# """
# (prev1, value1, next1) -> (prev2, value2, next2) -> (prev3, value3, next3) -> (prev4, value4, next4)
# """
#
#
# class DoubleConnectedNode:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev
#
