#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (List[List[int]]): List of boxes, each containing keys
    to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return False

    # Set to keep track of opened boxes
    opened_boxes = {0}

    # List to keep track of keys to explore
    keys_to_explore = boxes[0]

    while keys_to_explore:
        key = keys_to_explore.pop()

        # Skip if the key is out of bounds or already opened
        if 0 <= key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys_to_explore.extend(boxes[key])

    # Check if all boxes are opened
    return len(opened_boxes) == n
