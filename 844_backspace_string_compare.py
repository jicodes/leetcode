class Solution(object):
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Initialize 2 stacks to get the final characters for both the strings
        stack1 = []
        stack2 = []

        # Check for '#' character in the string and delete the character
        # if any from the stack
        for c in s:
            if c == "#":
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(c)

        for c in t:
            if c == "#":
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(c)

        # Check if both the stacks are same
        if stack1 == stack2:
            return True
        else:
            return False
