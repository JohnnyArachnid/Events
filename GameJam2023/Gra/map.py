import random
import math

def transponowanie_listy(map):
    temp_map = []
    for i in range(0, len(map[0])) :
        temp_map.append([])
        for j in range(0, len(map)) :
            if i == j :
                temp_map[i].append(map[i][j])
            else :
                temp_map[i].append(map[j][i])
    return temp_map

# map 12x12 tiles 256x256 pixel each
# map is surounded by 0, 0 is meant to be ignored, its purpose
# is to stop index out of range error and make it easier working with it
# on right and bottom neds to be "padding" of 0 equal to respectivly
# variables "number_of_tiles_in_a_row" and "number_of_tiles_in_a_column"
map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,7,3,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,5,5,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,7,3,3,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,6,6,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,7,3,3,3,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,2,1,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,3,3,8,5,5,5,5,5,5,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,1,2,1,2,1,2,1,2,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,3,3,2,6,6,6,6,6,6,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,1,2,1,2,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,2,1,2,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,4,1,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,1,2,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,4,2,1,2,1,2,1,2,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,2,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,4,1,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,5,5,5,2,1,2,1,2,1,2,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,6,6,6,1,2,1,2,1,2,7,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,1,2,1,2,1,2,7,3,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,2,1,2,1,2,7,3,8,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,1,2,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,1,2,1,2,7,3,8,2,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,2,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,2,1,2,7,3,8,2,1,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,1,2,1,2,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,1,2,7,3,8,2,1,2,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,2,1,2,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,2,7,3,8,2,1,2,1,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,3,2,1,2,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,7,3,8,2,1,2,1,2,3,3,1,2,1,2,1,2,1,2,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,3,1,2,1,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,7,3,8,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,3,3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,3,2,1,2,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

def set_student_groups(map, x, y):
    global studenciaki_biedaki
    if map[x][y] == 0 :
        map[x][y] = -1
        studenciaki_biedaki[str(x) + "_" + str(y)] = random.randint(0,8)
    if map[x - 1][y] == 0 :
        map[x - 1][y] = -1
        studenciaki_biedaki[str(x-1) + "_" + str(y)] = random.randint(0,8)
    if map[x + 1][y] == 0 :
        map[x + 1][y] = -1
        studenciaki_biedaki[str(x+1) + "_" + str(y)] = random.randint(0,8)
    if map[x][y - 1] == 0 :
        map[x][y - 1] = -1
        studenciaki_biedaki[str(x) + "_" + str(y-1)] = random.randint(0,8)
    if map[x][y + 1] == 0 :
        map[x][y + 1] = -1
        studenciaki_biedaki[str(x) + "_" + str(y+1)] = random.randint(0,8)

def distribute_students(map) :
    licznik_prob = 0
    player_pos_x_on_map = int( len(map) / 2 )
    player_pos_y_on_map = int( len(map[0]) / 2 )
    number_of_groups = random.randint(8,12)
    group_roots = [(player_pos_x_on_map,player_pos_y_on_map)]
    i = 0
    while i < number_of_groups :
        if licznik_prob > 50 :
            break
        licznik_prob += 1
        x = random.randint(10,55)
        y = random.randint(9,30)
        if map[x][y] != 0 :
            continue
        broken = False
        for group in group_roots :
            if math.sqrt(math.pow(group[0] - x,2) + math.pow(group[1] - y,2)) < 5 :
                i -= 1
                broken = True
                break
        if broken :
            continue
        set_student_groups(map, x, y)
        group_size = random.randint(1,4)
        j = 0
        while j < group_size :
            r = random.random()
            if r < 0.25 and x+1 < 55 and y+1 < 30 :
                set_student_groups(map, x+1,y+1)
            elif r < 0.5 and x+1 < 55 and y-1 > 9 :
                set_student_groups(map, x+1, y-1)
            elif r < 0.75 and x-1 > 10 and y-1 > 9 :
                set_student_groups(map, x-1, y-1)
            elif r < 0.75 and x-1 > 10 and y+1 < 30 :
                set_student_groups(map, x-1, y+1)
            j += 1
        
        i += 1



map = transponowanie_listy(map).copy()

# student
studenciaki_biedaki = dict([])

# map dimensions
map_width = len( map )
map_height = len( map[0] )
print(map_width, map_height)
# player default position 
player_pos_x_on_map = int( map_width / 2 )
player_pos_y_on_map = int( map_height / 2 )

structure_map_without_students = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,-2,12,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,-2,14,15,0,0,4,8,9,0,0,0,0,0,3,0,8,9,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,-2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,13,-3,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,-2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,14,15,-3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,2,0,0,0,10,11,4,0,0,0,0,4,0,10,11,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,13,-3,0,0,0,0,0,0,0,0],   
    [0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,15,-3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,-3,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,-3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,-3,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,-3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,13,-3,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,14,15,-3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,12,13,-3,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,13,0,0,0,12,13,0,0,0,12,13,0,0,0,0,0,0,0,0,0,14,15,-3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,7,0,0,0,0,0,14,15,0,0,0,14,15,0,0,0,14,15,0,0,0,0,7,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0],    
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0],   
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

def add_pucha(map,map_width,map_height, player_pos_x, player_pos_y, num_of_tiles_in_a_row, num_of_tiles_in_a_column) :
    # position_direction = random.random()
    
    # if position_direction < 1/4 :
    pos_x_puchy = random.randint(8,50)
    pos_y_puchy = random.randint(8,25)
    
    if map[pos_x_puchy][pos_y_puchy] == 0 :
        map[pos_x_puchy][pos_y_puchy] = 1
        
    # elif position_direction < 1/2 :
    #     pos_x_puchy = random.randint(player_pos_x + num_of_tiles_in_a_row,map_width - num_of_tiles_in_a_row)
    #     pos_y_puchy = random.randint(num_of_tiles_in_a_column,map_height - num_of_tiles_in_a_column)
        
    #     if map[pos_x_puchy][pos_y_puchy] == 0 :
    #         map[pos_x_puchy][pos_y_puchy] = 1
    # elif position_direction < 3/4 :
    #     pos_x_puchy = random.randint(num_of_tiles_in_a_row,map_width-num_of_tiles_in_a_row)
    #     pos_y_puchy = random.randint(player_pos_y + num_of_tiles_in_a_column,map_height - num_of_tiles_in_a_column)
        
    #     if map[pos_x_puchy][pos_y_puchy] == 0 :
    #         map[pos_x_puchy][pos_y_puchy] = 1
    # else :
    #     pos_x_puchy = random.randint(num_of_tiles_in_a_row,player_pos_x - num_of_tiles_in_a_row)
    #     pos_y_puchy = random.randint(num_of_tiles_in_a_column,player_pos_y - num_of_tiles_in_a_column)
        
    #     if map[pos_x_puchy][pos_y_puchy] == 0 :
    #         map[pos_x_puchy][pos_y_puchy] = 1

structure_map_without_students = transponowanie_listy(structure_map_without_students).copy()
structure_map = structure_map_without_students.copy()

distribute_students(structure_map)

def new_map(changed_map):
    random.seed()
    distribute_students(changed_map)
