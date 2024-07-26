def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    steps = []

