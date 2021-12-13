# these four functions return True if increasing, bounds if out of bounds, and False otherwise
def check_west(lines, col, row, bounds):
    if col == 0: return bounds
    if int(lines[row][col]) < int(lines[row][col-1]): return True
    else: return False

def check_north(lines, col, row, bounds):
    if row == 0: return bounds
    if int(lines[row][col]) < int(lines[row-1][col]): return True
    else: return False

def check_east(lines, col, row, bounds):
    if col + 1 == len(lines[row]): return bounds
    if int(lines[row][col]) < int(lines[row][col+1]): return True
    else: return False

def check_south(lines, col, row, bounds):
    if row + 1 == len(lines): return bounds
    if int(lines[row][col]) < int(lines[row+1][col]): return True
    else: return False

with open('input.txt') as file:
    lines = file.readlines()
    risk_total = 0
    for row in range(len(lines)):
        lines[row] = lines[row].strip()
        for col in range(len(lines[row])):
            if check_north(lines, col, row, True) and check_east(lines, col, row, True) and check_south(lines, col, row, True) and check_west(lines, col, row, True):
                risk_total += int(lines[row][col]) + 1
    print(risk_total)