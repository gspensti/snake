# Write the draw_map function to create a 10x10 grid and replace dots (.) with X for the snake's coordinates.
# Test the function with various inputs.


def draw_map(coordinates):
    rows = [] # initializes "big" list
    for row in range (10):  # outer loop initializes list of columns (smaller) list) within every row  (big list)
        columns = []
        for column in range (10):  
            columns.append(".")  # fills inner/smaller lists within every row with dots 
        rows.append(columns) # fills "big" list with now filled smaller list after range is done

    for x,y in coordinates: # replaces . for x on given coordinates 
        rows [x][y] = "X" # x = rows, y = columns

    for row in rows:
       print(row) # prints grid

draw_map([(0,0),(1,0),(2,2),(4,3),(8,9),(8,9)])

# 2 Write a movement function that gets the coordinates as a list and the direction keyword
# ('n','s','e','w') (north, south, east, west) and adds to that list, the last point “moved” - added
# in that direction. 

def move (coordinates, letter):
    x_axis_coord = coordinates [-1][0]  # stores first item (0) of last (-1) tuple in list in new variable 
    y_axis_coord = coordinates [-1][1]  # stores secind (1) item of last (-1) tuple in list in new variable  

    if letter == 'e': # move right --> columns adds + 1
        coord_tuple = (x_axis_coord, (y_axis_coord + 1)) # stores changes x & y values in new tuple 
    if letter == 'w': # move left --> columns decrease 1
        coord_tuple = (x_axis_coord, (y_axis_coord - 1)) # stores changes x & y values in new tuple 
    if letter == 's': # move down --> rows add + 1
        coord_tuple = ((x_axis_coord + 1), y_axis_coord) # stores changes x & y values in new tuple 
    if letter == 'n': # move up --> rows add -1 
        coord_tuple = ((x_axis_coord - 1), y_axis_coord) # stores changes x & y values in new tuple 
    coordinates.append(coord_tuple) # appends list of coordinates with newly created tuple containing changed values for x & y (appends adds to end of list)
    print(coordinates) # just for testing!

        
move ([(0,0)], 'e')
move ([(0,0),(0,1),(0,2)], 'e')
move ([(0,0),(0,1),(0,2)], 's')



