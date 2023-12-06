"""Day 3 solution"""
SCHEMATIC = [line.strip() for line in open("input.txt", "r").readlines()]  # Add input.txt in the directory
ROWS = len(SCHEMATIC)
COLUMNS = len(SCHEMATIC[0])
valid_positions = []


# ------------------ FUNCTIONS ------------------
def add_symbols(row_n, col_n):
    """Calculates the 'area of infulence' of a found symbol"""
    positions = []
    for r in range(row_n-1, row_n+2):
        if 0 <= r <= ROWS:
            for c in range(col_n-1, col_n+2):
                if 0 <= c <= COLUMNS:
                    positions.append((r,c))
    return positions


def add_digit_gear(digit_string, positions):
    for gear in gears:
        if bool(set(gear['positions']) & set(positions)):
            gear['parts'].append(int(digit_string))


# ------------------ PROGRAM ------------------
# Parse valid positions
for i in range(ROWS):
    for j, symbol in enumerate(SCHEMATIC[i]):
        if symbol not in '0123456789.':
            valid_positions += add_symbols(i,j)
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

# Parse possible gears
gears = []
for i in range(ROWS):
    for j, symbol in enumerate(SCHEMATIC[i]):
        if symbol == '*':
            gears.append({'parts': [], 'positions': add_symbols(i,j)})

# Add parts to possible gears
for i, line in enumerate(SCHEMATIC):
    digit_buffer = ""
    digit_positions = []
    for j, symbol in enumerate(line):
        if symbol in '0123456789':
            digit_buffer += symbol
            digit_positions.append((i,j))
            if j+1 == COLUMNS:
                add_digit_gear(digit_buffer,digit_positions)
        else:
            if len(digit_buffer) > 0:
                add_digit_gear(digit_buffer,digit_positions)
            digit_buffer = ""
            digit_positions = []

# Get gear ratios
gear_ratio_total = 0
for gear in gears:
    if len(gear['parts']) == 2:
        gear_ratio_total += gear['parts'][0] * gear['parts'][1]

print(f'Total parts: {total}')
print(f'Total gear ratio: {gear_ratio_total}')
