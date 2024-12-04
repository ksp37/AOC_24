from aocd import data

REVERSE_XMAS = 'SAMX'
FORWARD_XMAS = 'XMAS'
CROSSED_MAS = ("MAS", "SAM")

EXAMPLE = [
"MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]

def find_xmas(row_idx, col_idx, data):
    num_xmas_found = 0
    row_max = len(data)
    col_max = len(data[row_idx])
   
   
    if col_idx > 2:
        #left horizontal
        if data[row_idx][col_idx-3:col_idx+1] == REVERSE_XMAS:
            num_xmas_found += 1

        # top left diagonal
        if row_idx > 2 and "".join(data[row_idx-idx][col_idx-idx] for idx in range(0,4)) == FORWARD_XMAS:
            num_xmas_found += 1
            print(row_idx, col_idx, "TOP LEFT")

        # bottom left diagonal
        if row_idx + 3 < row_max and "".join(data[row_idx+idx][col_idx-idx] for idx in range(0,4)) == FORWARD_XMAS:
            num_xmas_found += 1
            print(row_idx, col_idx, "BOTTOM LEFT")

    
    if col_idx + 3 < col_max:
        #right horizontal 
        if data[row_idx][col_idx:col_idx+4] == FORWARD_XMAS:
            num_xmas_found += 1

        # top right diagonal
        if row_idx > 2 and "".join(data[row_idx-idx][col_idx+idx] for idx in range(0,4)) == FORWARD_XMAS:
            num_xmas_found += 1
            print(row_idx, col_idx, "TOP RIGHT")

        # bottom right diagonal
        if row_idx + 3 < row_max and "".join(data[row_idx+idx][col_idx+idx] for idx in range(0,4)) == FORWARD_XMAS:
            num_xmas_found += 1
            print(row_idx, col_idx, "BOTTOM RIGHT")

    
    if row_idx > 2:
        # top vertical
        if "".join(data[_row_idx][col_idx] for _row_idx in range(row_idx-3,row_idx+1)) == REVERSE_XMAS: 
            num_xmas_found += 1

    
    if row_idx + 3 < row_max:
        #bottom vertical 
        if "".join(data[_row_idx][col_idx] for _row_idx in range(row_idx,row_idx+4)) == FORWARD_XMAS:
            num_xmas_found += 1

    return num_xmas_found

def find_x_mas(row_idx, col_idx, data):
    num_xmas_found = 0
    row_max = len(data)
    col_max = len(data[row_idx])
    if row_idx >= 1 and col_idx >= 1 and row_idx + 1 < row_max and col_idx + 1 < col_max:
        if "".join(data[row_idx + idx][col_idx + idx] for idx in range(-1,2)) in CROSSED_MAS and "".join(data[row_idx + (-1)*idx][col_idx + idx] for idx in range(-1,2)) in CROSSED_MAS:
            num_xmas_found += 1

    return num_xmas_found

if __name__ == "__main__":
    puzzle = data.split("\n")
    total = 0 
    for row_idx, row in enumerate(puzzle):
        for col_idx, col in enumerate(row):
            if puzzle[row_idx][col_idx] == "X":
                total += find_xmas(row_idx, col_idx, puzzle)

    print(f"Part 1: {total}")

    total = 0 
    for row_idx, row in enumerate(puzzle):
        for col_idx, col in enumerate(row):
            if puzzle[row_idx][col_idx] == "A":
                total += find_x_mas(row_idx, col_idx, puzzle)

    print(f"Part 2: {total}")