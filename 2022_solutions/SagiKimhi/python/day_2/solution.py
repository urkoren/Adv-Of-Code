#################################
#           Imports             #
#################################
from enum import Enum
from dataclasses import dataclass


#################################
#     Variable Definitions      #
#################################

# Enum classes
class Option(Enum):
    ROCK        = 1
    PAPER       = 2
    SCISSORS    = 3

    def next(self):
        if self.value==Option.SCISSORS.value:
            return Option.ROCK
        
        return Option(self.value+1)

    def prev(self):
        if self.value==Option.ROCK.value:
            return Option.SCISSORS
        
        return Option(self.value-1)

class Outcome(Enum):
    LOSS        = 0
    DRAW        = 3
    WIN         = 6

# Dictionaries mapping between a character and it's correspending Option Item
SELF_CHOICE_DICT        = {'X':Option.ROCK, 'Y':Option.PAPER, 'Z':Option.SCISSORS}
OPPONENT_CHOICE_DICT    = {'A':Option.ROCK, 'B':Option.PAPER, 'C':Option.SCISSORS}

# Dictionary mapping between a character and its corresponding Outcome item
DESIRED_OUTCOME_DICT    = {'X':Outcome.LOSS, 'Y':Outcome.DRAW, 'Z':Outcome.WIN}

# Other Variables
INPUT_FILENAME = 'input.txt'


#################################
#      Function Definitions     #
#################################
def get_opponent_option(choice: str) -> Option:
    global OPPONENT_CHOICE_DICT

    if (choice not in OPPONENT_CHOICE_DICT):
        raise Exception
    
    return OPPONENT_CHOICE_DICT[choice]

def get_self_option(choice: str) -> Option:
    global SELF_CHOICE_DICT

    if (choice not in SELF_CHOICE_DICT):
        raise Exception
    
    return SELF_CHOICE_DICT[choice]

def get_desired_outcome(key: str) -> Outcome:
    global DESIRED_OUTCOME_DICT

    if (key not in DESIRED_OUTCOME_DICT):
        raise Exception
    
    return DESIRED_OUTCOME_DICT[key]

def get_self_choice_score(choice: str) -> int:
    return get_self_option(choice).value

def get_opponent_choice_score(choice: str) -> int:
    return get_opponent_option(choice).value

def get_self_outcome(opponent_option: Option, self_option: Option) -> Outcome:
    if (self_option==opponent_option.next()):
        return Outcome.WIN
    
    if (self_option==opponent_option):
        return Outcome.DRAW

    return Outcome.LOSS

def get_opponent_outcome(opponent_option: Option, self_option: Option) -> Outcome:
    return get_self_outcome(self_option, opponent_option)

def get_option_by_desired_outcome(opponent_option: Option,desired_outcome: Outcome) -> Option:
    if (desired_outcome==Outcome.WIN):
        return opponent_option.next()

    if (desired_outcome==Outcome.DRAW):
        return opponent_option
    
    return opponent_option.prev()

def get_self_score(opponent_choice: str, self_choice: str) -> int:
    return (
        get_self_choice_score(self_choice) +
        get_self_outcome(get_opponent_option(opponent_choice), get_self_option(self_choice)).value
    )

def get_opponent_score(opponent_choice: str, self_choice: str) -> int:
    return (
        get_opponent_choice_score(opponent_choice) +
        get_opponent_outcome(get_opponent_option(opponent_choice), get_self_option(self_choice)).value
    )

def get_choices(line: str):
    choices = line.strip().split()
    
    if (len(choices)!=2):
        raise Exception
    
    return choices[0], choices[1]


#################################
#           SOLUTIONS           #
#################################
def part_one_solution():
    global INPUT_FILENAME

    total_score = 0

    with open(INPUT_FILENAME) as file:
        for line in file:
            (
                opponent_choice, 
                self_choice 
            )           = get_choices(line)
            total_score += get_self_score(opponent_choice, self_choice)

    print(f'total score of part one solution is: {total_score}')

def part_two_solution():
    global INPUT_FILENAME

    total_score = 0

    with open(INPUT_FILENAME) as file:
        for line in file:
            (
                opponent_choice, 
                outcome_key
            )               = get_choices(line)
            opponent_option = get_opponent_option(opponent_choice)
            desired_outcome = get_desired_outcome(outcome_key)
            self_option     = get_option_by_desired_outcome(opponent_option, desired_outcome)
            total_score     += self_option.value + desired_outcome.value

    print(f'total score of part two solution is: {total_score}')


#################################
#             MAIN              #
#################################
if __name__ == '__main__':
    part_one_solution()
    part_two_solution()
