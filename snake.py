# Write the draw_map function to create a 10x10 grid and replace dots (.) with X for the snake's coordinates.
# Test the function with various inputs.


def draw_map(coordinates):
    rows = [] # initializes "big" list
    for row in range (10):  # outer loop initializes list of columns (smaller) list) within every row  (big list)
        columns = []
        for column in range (10):  
            columns.append(".")  # fills inner/smaller lists within every row with dots 
        rows.append(columns) # fills "big" list with now filled smaller list after range is done

    for x,y in coordinates:
        rows [x][y] = "X"

    for row in rows:
       print(row)

draw_map([(0,0),(1,0),(2,2),(4,3),(8,9),(8,9)])
