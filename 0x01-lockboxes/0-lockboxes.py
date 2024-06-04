#!/usr/bin/python3
"""
Solution for lockboxes task
"""


def canUnlockAll(boxes):
    """
    Determines if the  locked boxes can be opened
    based on keysto the other boxes. 
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for b in range(1, len(boxes) - 1):
        checked_boxes = False
        for i in range(len(boxes)):
            checked_boxes = b in boxes[i] and b != i
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
