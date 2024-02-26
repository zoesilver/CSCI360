# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque
import heapq
import copy

def calculateh(stack):
    count = 0
    for i in range(len(stack.order)):
        #ensure it's not the last item in the stack
        if i!=len(stack.order)-1:
            #if not adjacent
            if stack.order[i]+1!=stack.order[i+1] and stack.order[i]-1!=stack.order[i+1]:
                count=count+1
            #if orientations are not the same
            elif stack.orientations[i]!=stack.orientations[i+1]:
                count = count+1
            #wrong order, right orientation
            elif stack.orientations[i]==1 and stack.orientations[i+1]==1 and stack.order[i]+1!=stack.order[i+1]:
                count = count+1
            #right order, wrong orientation
            elif (stack.orientations[i]==0 or stack.orientations[i+1]==0) and stack.order[i]+1==stack.order[i+1]:
                count = count+1
    return count

def a_star_search(stack):

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    pq=[]
    flips = 0
    hVal = calculateh(stack)
    fVal = flips+hVal
    flippedOn = 0
    visited = []
    temp_seq = []
    heapq.heappush(pq, (fVal, flips, hVal, flippedOn, temp_seq))
    while len(pq)!=0:
        inspecting = heapq.heappop(pq)
        #check if it's been seen before
        if inspecting[4] in visited:
            continue
        #add to seen list
        visited.append(inspecting)
        tempStack = stack.copy()
        #flip to initial state to inspect
        for i in range(len(inspecting[4])):
            tempStack.flip_stack(inspecting[4][i])
        if tempStack.check_ordered():
            stack=tempStack.copy()
            flip_sequence = inspecting[4][:]
            return flip_sequence
        #create new sequence for all possible flip locations
        # add flip location to sequence
        #push onto the heap
        for i in range(len(stack.order)):
            temp_seqCopy = inspecting[4][:]
            tempStack2 = tempStack.copy()
            tempStack2.flip_stack(i+1)
            temp_seqCopy.append(i+1)
            flips = inspecting[1]+1
            #update hval
            hVal=calculateh(tempStack2)
            flippedOn = i
            #add to heap
            heapq.heappush(pq,(flips+hVal, flips, hVal, flippedOn, temp_seqCopy))


    return flip_sequence

    # ---------------------------- #


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
