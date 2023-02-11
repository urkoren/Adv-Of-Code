# By the time you calculate the answer to the Elves' question, 
# they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know 
# the total Calories carried by the top three Elves carrying the most Calories. 
# That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above (see part one doc), the top three Elves are the fourth Elf (with 24000 Calories), 
# then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). 
# The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
from dataclasses        import dataclass
from part_one_solution  import is_new_elf

@dataclass
class elf:
    elf_num:    int
    calories:   int = 0

    def __add__(self, other):
        try:
            return elf(self.calories + other.calories)
        except:
            return elf(self.calories+other)


input_filename              = 'input.txt'
total_nof_elves             = 0
top_three_elves    = [elf(0,0) for i in range(3)]

with open(input_filename, 'r') as file:
    curr_count      = 0
    previous_line   = ''

    for line in file:
        if is_new_elf(line, previous_line, total_nof_elves):
            curr_count      = 0
            total_nof_elves += 1
        
        previous_line = line

        if line.isspace():
            top_three_elves.sort(key=lambda _elf: _elf.calories)

            for val in top_three_elves:
                if val.calories<curr_count:
                    val.calories    = curr_count
                    val.elf_num     = total_nof_elves
                    break
            
            continue
        
        curr_count += int(line.strip())

top_three_elves.sort(key=lambda _elf: _elf.calories, reverse=True)
print("\nThe top three elves are", end=' ')

for i, _elf in enumerate(top_three_elves):
    num_postfix_str = 'st' if _elf.elf_num%10==1 else 'nd' if _elf.elf_num%10==2 else 'rd' if _elf.elf_num%10==3 else 'th'
    print(f'the {_elf.elf_num}{num_postfix_str} elf with {_elf.calories} calories', end=', then ' if i<len(top_three_elves)-1 else '.\n')

print(f'The sum of calories carried by these three elves is: {sum(e.calories for e in top_three_elves)}\n')
