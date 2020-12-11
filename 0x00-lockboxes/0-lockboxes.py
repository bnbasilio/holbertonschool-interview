#!/usr/bin/python3
''' 0-lockboxes.py '''


def canUnlockAll(boxes):

    if not boxes:
        return False
    open = [False] * len(boxes)
    open[0] = True
    keys = [0]
    while keys:
        checked = keys.pop()
        for key in boxes[checked]:
            if key < len(boxes) and not open[key]:
                open[key] = True
                keys.append(key)
    result = all(open)
    return result
