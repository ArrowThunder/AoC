def open_to_close(char):
    if char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'
    elif char == '<':
        return '>'
    else:
        return None

with open('input.txt') as file:
    corrupt_score = 0
    incomplete_scores = []
    for line in file:
        line = line.strip()
        chunk_stack = []
        corrupt = False
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                chunk_stack.append(char)
            else:
                if open_to_close(chunk_stack.pop()) == char:
                    continue
                else:
                    corrupt = True
                if char == ')':
                    corrupt_score += 3
                elif char == ']':
                    corrupt_score += 57
                elif char == '}':
                    corrupt_score += 1197
                elif char == '>':
                    corrupt_score += 25137
                break
        if not corrupt:
            score = 0
            while len(chunk_stack) > 0:
                to_add = open_to_close(chunk_stack.pop())
                score *= 5
                if to_add == ')':
                    score += 1
                elif to_add == ']':
                    score += 2
                elif to_add == '}':
                    score += 3
                elif to_add == '>':
                    score += 4
            incomplete_scores.append(score)
    print(corrupt_score)
    incomplete_scores.sort()
    print(incomplete_scores[int(len(incomplete_scores)/2)])