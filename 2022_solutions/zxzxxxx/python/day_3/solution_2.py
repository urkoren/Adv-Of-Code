output          = 0
match_letters   = []
number          = 0
input_file      = "input.txt"
common_letter = " "



def split_string(line):
    len_str = len(line)
    # if len_str % 2 == 0:
    str1 = line[0:len_str//2]
    str2 = line[len_str//2:]
    return str1, str2
 
        
def check_match_latters(strings: list[str]):
    global common_letter
    str_set = ""
    
    if len(strings) == 0:
        return None

    for i in range(len(strings)):
        if i == 0:
            str_set = set(strings[0])        
            continue
            
        common_letter = str_set&set(strings[i])
        print(common_letter)
    
    
def check_upper_lower_case(character): 
    if character.isupper():
        return True
    else:
        return False
        
def convert_numbers(common_letter):
    global output
    print(common_letter)
    if check_upper_lower_case(common_letter):
        number = ord(common_letter.lower()) - 96
        number += 26
        output += number
    else:
        number = ord(common_letter) - 96
        output += number
    
        
def sulution():
    global input_file
    with open(input_file, "r") as file:
        for line in file:
            str1, str2 = split_string(line)
            check_match_latters([str1, str2])
            convert_numbers()
            
def sulution_2():
    global input_file
    number_of_lines_to_match = 3
    strings = []
    with open(input_file, "r") as file:
        for i, line in enumerate(file):
            strings.append(str(line))
            print(i)
            print(line)
            if i % number_of_lines_to_match == 0:
                check_match_latters(strings)
                print(strings)
                convert_numbers(common_letter)
                strings = []
                
       
# sulution()
sulution_2()
print(output)


