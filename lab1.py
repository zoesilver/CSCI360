# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque

def depth_first_search(stack):
    flip_sequence = []
    # # --- v ADD YOUR CODE HERE v --- #
    visited = []
    toSee = []

    toSee.append((stack.copy(), 0))
    while len(toSee) != 0:
        examiningW = toSee.pop()
        examining = examiningW[0]
        if examining not in visited:
            if examiningW[1]!=0:
                flip_sequence.append(examiningW[1])
        else:
            continue
        if examining.check_ordered():
            stack=examining.copy()
            return flip_sequence


        visited.append(examining.copy())

        for num in range(len(stack.order)):
            temp = examining.copy()
            temp.flip_stack(num+1)

            toSee.append((temp.copy(), num+1))

    for x in flip_sequence:
        print(x)
    return flip_sequence
    # ---------------------------- #
