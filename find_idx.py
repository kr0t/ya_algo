def solution(node, elem):
    idx = 0
    while node:
        if node.value == elem:
            return idx
        else:
            node = node.next_item
            idx += 1
    return -1
