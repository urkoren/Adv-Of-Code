input_file      = "input.txt"
sum             = 0

def arrange(line):
    ranges = []
    b = line.split(",")
    for i in range(len(b)):
        d = b[i].split("-")
        for i in range(len(d)):
            ranges.append(int(d[i]))
    return ranges

def check_if_match(ranges):
    global sum
    
    if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
        sum += 1
        return
        
    elif ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
        sum += 1
        return
    
    else:
        return

def check_if_contain(ranges):
    global sum
    
    if ranges[0] <= ranges[2] and ranges[1] >= ranges[2]:
        sum += 1
        return
        
    elif ranges[2] <= ranges[0] and ranges[3] >= ranges[0]:
        sum += 1
        return
    
    else:
        return
    
def solution():
    global input_file,sum
    with open(input_file, "r") as file:
        for line in file:
            check_if_match(arrange(line))
    print(sum)
    sum = 0
            

def solution_2():
    global input_file,sum
    with open(input_file, "r") as file:
        for line in file:
            check_if_contain(arrange(line))
    print(sum)
    sum = 0

            
solution()
solution_2()