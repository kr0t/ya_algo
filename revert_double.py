def solution(node):
    if not node:
        return node
    node.next, node.prev = node.prev, node.next
    if not node.prev:
        return node
    return solution(node.prev)