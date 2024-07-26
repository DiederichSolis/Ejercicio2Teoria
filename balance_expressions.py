def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    steps = []

    for char in expression:
        if char in '([{':
            stack.append(char)
            steps.append(f"Push: {char}, Stack: {stack}")
        elif char in ')]}':
            if stack and stack[-1] == pairs[char]:
                stack.pop()
                steps.append(f"Pop: {char}, Stack: {stack}")
            else:
                steps.append(f"Unmatched: {char}, Stack: {stack}")
                return False, steps
    steps.append(f"Final Stack: {stack}")
    return not stack, steps

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        balanced, steps = is_balanced(line)
        print(f"Line {line_number}: {line}")
        for step in steps:
            print(step)
        print(f"Balanced: {balanced}\n")

# Ruta del archivo de texto
file_path = 'expressions.txt'
process_file(file_path)
