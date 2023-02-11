draw                    = 3
lose                    = 0
win                     = 6
shape_you_selected      = 0
total_score             = 0
rock                    = 1
paper                   = 2
scissors                = 3
status                  = 0
input_file              = "input.txt"

def sum_score() -> None:
    global total_score
    
    total_score += status
    total_score += shape_you_selected

def check_winner(line) -> None:
    global status
    
    if line[0] == line[1]:
        status = draw
    
    elif line[1] - line[0] == 1 or line[0] - line[1] == 2:
        status = win
        
    elif line[0] - line[1] == 1 or line[1] - line [0] == 2:
        status = lose
    
def define_pc_shape(line) -> None:
    
    if line[0] == "A":
        line[0] = rock
    
    elif line[0] == "B":
        line[0] = paper
        
    elif line[0] == "C":
        line[0] = scissors   
        
def define_player_shape(line) -> None:
    global shape_you_selected
    
    if line[1] == "X":
        line[1] = rock
        shape_you_selected = line[1]
    
    elif line[1] == "Y":
        line[1] = paper
        shape_you_selected = line[1]
        
    elif line[1] == "Z":
        line[1] = scissors   
        shape_you_selected = line[1]
        
def define_player_shape_2(line) -> None:
    global shape_you_selected
    
    #draw
    if line[1] == "Y":
        line[1] = line[0]
        shape_you_selected = line[1]
      
    #lose  
    elif line[1] == "X":
        if line[0] == 3 or line[0] == 2:
            line[1] = line[0] - 1
        else:
            line[1] = 3
        shape_you_selected = line[1]
            
    #win
    elif line[1] == "Z":
        if line[0] == 1 or line[0] == 2:
            line[1] = line[0] + 1
        else:
            line[1] = 1
        shape_you_selected = line[1]
        
def solution_1():
    global input_file
    
    with open(input_file, "r") as file:
        for line_full in file:
            line = line_full.split()
            define_pc_shape(line)
            define_player_shape(line)
            check_winner(line)
            sum_score()        
            
def solution_2():
    global input_file
    
    with open(input_file, "r") as file:
        for line_full in file:
            line = line_full.split()
            define_pc_shape(line)
            define_player_shape_2(line)
            check_winner(line)
            sum_score()
            
solution_2()
print(total_score)

        
          