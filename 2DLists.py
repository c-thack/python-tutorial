number_grid = [  # 4 rows, 3 columns
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])  # row, column

for row in number_grid:  # loop through the 2d list
    for col in row:
        print(col)
