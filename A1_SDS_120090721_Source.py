import random

t_list = [] # create a list for saving the puzzle
move_dict = {} # used to change direction
g_line = 0 # global variable for changing lines
g_column = 0 # global variable for changing column
g_dimension = 0 # global variable for users to give the dimention

def get_list(t_list): # create ordered puzzle
    global g_dimension
    t_list = [[]for i in range(g_dimension)]
    for i in range(g_dimension):
        for j in range(1,g_dimension**2):
            if i*g_dimension+1 <= j < (i+1)*g_dimension+1:
                t_list[i].append(j)
    t_list[g_dimension-1].append(' ')
    return t_list

def moving(move):# let the puzzle move
    global g_line, g_column
    if move == 2 and g_dimension > g_dimension - (g_line+1) > 0: # moving the empty space upward
        t_list[g_dimension-1-g_line][g_dimension-1-g_column], t_list[g_dimension-1-(g_line+1)][g_dimension-1-g_column] = \
            t_list[g_dimension-1-(g_line+1)][g_dimension-1-g_column], t_list[g_dimension-1-g_line][g_dimension-1-g_column]
        g_line = g_line + 1
        return True
    elif move == 0 and g_dimension > g_dimension-(g_column+1) > 0: # moving the empty space leftward
        t_list[g_dimension-1-g_line][g_dimension-1-g_column], t_list[g_dimension-1-g_line][g_dimension-1-(g_column+1)] = \
            t_list[g_dimension-1-g_line][g_dimension-1-(g_column+1)], t_list[g_dimension-1-g_line][g_dimension-1-g_column]
        g_column = g_column+1
        return True
    elif move == 3 and 1 < g_dimension-(g_line-1) < g_dimension+1: # moving the empty space downward
        t_list[g_dimension-1-g_line][g_dimension-1-g_column], t_list[g_dimension-1-(g_line-1)][g_dimension-1-g_column] = \
            t_list[g_dimension-1-(g_line-1)][g_dimension-1-g_column], t_list[g_dimension-1-g_line][g_dimension-1-g_column]
        g_line = g_line-1
        return True
    elif move == 1 and 1 < g_dimension-(g_column-1) < g_dimension+1: # moving the empty space rightward
        t_list[g_dimension-1-g_line][g_dimension-1-g_column], t_list[g_dimension-1-g_line][g_dimension-1-(g_column-1)] = \
            t_list[g_dimension-1-g_line][g_dimension-1-(g_column-1)], t_list[g_dimension-1-g_line][g_dimension-1-g_column]
        g_column = g_column-1
        return True
    else:
        return False

def print_graph(): # print the puzzle beautifully
    for i in range(len(t_list)):
        for j in range(len(t_list[i])):
            print(t_list[i][j],end='\t')
        print()
    return

def get_game(): # upset the ordered list to get a puzzle
    global g_dimension, g_column, g_count, g_line
    i = 0 # use i to count the vaild upsetings
    while i <= g_dimension**4:
        x = random.randint(0,3)
        if moving(x) is True:
            i += 1
        else:
            i = i
    print_graph()
    return

print('Welcome to the puzzle game!')

while True: # let users input the dimention
    g_dimension = input('please give a dimention(from 3 to 10) of the puzzle:')
    try:
        g_dimension = int(g_dimension)
        if 3 <= g_dimension <= 10:
            break
        else:
            print('the dimention should be a integer from 3 to 10')
            continue
    except:
        print('the dimention should be a integer from 3 to 10')

while True: # let users input four letters which represent the directions
    move = input('Enter four different letters used for left, right, up and down directions(do not space between characters):')
    k = 0
    for i in range(len(move)):
        move_dict[move[i]] = k
        k += 1
    if len(move_dict.keys())==4 and move.isalpha():
        break
    else:
        move_dict.clear()
        print('there should be four directions which are represented by different letters. Please do not Seperate them by space when typing in.')

answer = []
answer = get_list(answer) # get the correct answer
t_list = get_list(t_list)
get_game() # upset the list and turn it into a puzzle
c=0 #count how many steps the users move

while True: # let users solve the puzzle
    if t_list==answer: # test if the puzzle is solved
        print('Congratulation! You use',c,'moves to solve the puzzle!')
        break
    g_move = input('Enter your move:')
    try: # let users move the space
        if moving(move_dict[g_move]):
            print_graph()
            c+=1
        else:
            print('the movement is invalid.')
    except: # avoid invaild input
         print('the movement is invalid.')

input('press enter to exit')