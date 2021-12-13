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
    if col + 1 == len(lines[0]): return bounds
    if int(lines[row][col]) < int(lines[row][col+1]): return True
    else: return False

def check_south(lines, col, row, bounds):
    if row + 1 == len(lines): return bounds
    if int(lines[row][col]) < int(lines[row+1][col]): return True
    else: return False
    
def define_basin(lines, col, row, contents):
    if int(lines[row][col]) == 9:
        return
    if (col,row) in contents:
        return
    contents.append((col,row))
    if check_north(lines, col, row, False):
        define_basin(lines, col, row - 1, contents)
    if check_east(lines, col, row, False):
        define_basin(lines, col + 1, row, contents)
    if check_south(lines, col, row, False):
        define_basin(lines, col, row + 1, contents)
    if check_west(lines, col, row, False):
        define_basin(lines, col - 1, row, contents)   

with open('input.txt') as file:
    lines = file.readlines()
    basin_1st = []
    basin_2nd = []
    basin_3rd = []
    for row in range(len(lines)):
        lines[row] = lines[row].strip()
        for col in range(len(lines[row])):
            if check_north(lines, col, row, True) and check_east(lines, col, row, True) and check_south(lines, col, row, True) and check_west(lines, col, row, True):
                new_basin = []
                define_basin(lines, col, row, new_basin)
                if len(new_basin) > len(basin_1st):
                    basin_3rd = basin_2nd
                    basin_2nd = basin_1st
                    basin_1st = new_basin.copy()
                elif len(new_basin) > len(basin_2nd):
                    basin_3rd = basin_2nd
                    basin_2nd = new_basin.copy()
                elif len(new_basin) > len(basin_3rd):
                    basin_3rd = new_basin.copy()
    print(len(basin_1st)*len(basin_2nd)*len(basin_3rd))