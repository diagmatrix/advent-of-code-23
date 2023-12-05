"""Day 3 solution"""
SCHEMATIC = [line.strip() for line in open("input.txt", "r").readlines()]
ROWS = len(SCHEMATIC)
COLUMNS = len(SCHEMATIC[0])

valid_positions = []

def add_symbols(row_n, col_n):
    """Calculates the 'area of infulence' of a found symbol"""
    for r in range(row_n-1, row_n+2):
        if 0 <= r <= ROWS:
            for c in range(col_n-1, col_n+2):
                if 0 <= c <= COLUMNS:
                    valid_positions.append((r,c))

# Parse valid positions
for i in range(ROWS):
    for j, symbol in enumerate(SCHEMATIC[i]):
        if symbol not in '0123456789.':
            add_symbols(i,j)
valid_positions = list(set(valid_positions))

# Parse schematic for digits
total = 0
for i, line in enumerate(SCHEMATIC):
    digit_buffer = ""
    valid_part = False
    for j, symbol in enumerate(line):
        if symbol in '0123456789':
            digit_buffer += symbol
            valid_part = valid_part or (i,j) in valid_positions
            if j+1 == COLUMNS and valid_part:
                total += int(digit_buffer)
                valid_part = False
        else:
            if len(digit_buffer) > 0 and valid_part:
                total += int(digit_buffer)
                valid_part = False
            digit_buffer = ""

print(total)
