#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    keys = boxes[0]

    while keys:
        box_to_open = keys.pop(0)
        if not visited[box_to_open]:
            visited[box_to_open] = True
            keys.extend(boxes[box_to_open])

    return all(visited)

