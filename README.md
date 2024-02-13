This is the work I've completed for CSCI360: Introduction to Artificial Intelligence

Project 1: Textbook Stack
I recieved a vector of "textbook" objects and another vector indicating if each textbook is face up (1) or face down (0). When a textbook in the stack is flipped, all textbooks above it in the vector are reversed and their face-status is flipped. For example:
2 1 
3 0
1 1
0 0
If we flip the textbook at position 2, the result will be:
1 0
3 1
2 0
0 0
The correct outcome is:
0 1
1 1
2 1
3 1
I solved this problem using both breadth and depth first search.
