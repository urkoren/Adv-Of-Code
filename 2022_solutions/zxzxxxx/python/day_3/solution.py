output          = 0
match_letters   = []
number          = 0
input_file      = "input.txt"
three_lines     = 0
prime_match     = " "

def split_string(line):
    global match_letters
    len_str = len(line)
    # if len_str % 2 == 0:
    str1 = line[0:len_str//2]
    str2 = line[len_str//2:]
    a=list(set(str1)&set(str2))
    for i in a:
        print(i)
        match_letters.append(i)
        print(match_letters)
        
def check_letter():
    global match_letters, prime_match
    for i in match_letters:
        count = match_letters.count(i)
        if count > 1:
            prime_match = i
            print(prime_match)
            
       
def swap_match_letters():
    global prime_match, match_letters
    print(match_letters)
    print(prime_match)
    match_letters = []
    match_letters.append(prime_match)
    
def check_upper_lower_case(character): 
    if character.isupper():
        return True
    else:
        return False
        
def convert_numbers():
    global output, match_letters
    for character in match_letters:
        if check_upper_lower_case(character):
            print(match_letters)
            number = ord(character.lower()) - 96
            number += 26
            output += number
        else:
            number = ord(character) - 96
            output += number
      
def sulution():
    global input_file, match_letters
    with open(input_file, "r") as file:
        for line in file:
            split_string(line)
            convert_numbers()
            match_letters   = []  
            
def sulution_2():
    global input_file, three_lines, match_letters
    with open(input_file, "r") as file:
        for line in file:
            split_string(line)
            three_lines += 1
            print (three_lines)
            if three_lines >= 3:
                three_lines = 0
                check_letter()
                swap_match_letters()
                convert_numbers()
                match_letters   = []
            
# sulution()
sulution_2()
print(output)


