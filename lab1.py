# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque


def breadth_first_search(stack):
    flip_sequence = []
    # --- v ADD YOUR CODE HERE v --- #
    temp = stack.copy()
    for num in range(len(temp.order) - 1, -1, -1):
        found = False

        for x in range(len(temp.order)):
            if found:
                continue

                return flip_sequence
            if num == temp.order[x]:
                found = True
                if x != 0:
                    temp.flip_stack(x + 1)
                    flip_sequence.append(x + 1)

                if temp.orientations[x] == 1:
                    temp.flip_stack(1)
                    flip_sequence.append(1)

                temp.flip_stack(num + 1)
                flip_sequence.append(num + 1)

                continue


    return flip_sequence
    # ---------------------------- #


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