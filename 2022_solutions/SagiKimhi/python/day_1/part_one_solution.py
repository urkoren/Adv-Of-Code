# The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. 
# As your boats approach land, the Elves begin taking inventory of their supplies. 
# One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

# The Elves take turns writing down the number of Calories contained by the 
# various meals, snacks, rations, etc. that they've brought with them, one item per line. 
# Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.
# For example, suppose the Elves finish writing their items' Calories and end up with the following list:

# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# This list represents the Calories of the food carried by five Elves:
# The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
# The second Elf is carrying one food item with 4000 Calories.
# The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
# The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
# The fifth Elf is carrying one food item with 10000 Calories.
# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
# they'd like to know how many Calories are being carried by the Elf carrying the most Calories. 
# In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

input_file_name         = "input.txt"
total_nof_elves         = 0
most_calories_val       = 0
most_calories_idx       = 0

def is_new_elf(line: str, previous_line: str, nof_elves: int) -> bool:
    if line.isspace():
        return False
    
    if nof_elves==0 or previous_line.isspace():
        return True

    return False


with open(input_file_name, "r") as file_in:
    curr_calories_cnt   = 0
    previous_line       = ""

    for line in file_in:
        if is_new_elf(line, previous_line, total_nof_elves):
            curr_calories_cnt   = 0
            total_nof_elves     += 1
        
        previous_line = line

        if line.isspace():
            if most_calories_val < curr_calories_cnt:
                most_calories_val   = curr_calories_cnt
                most_calories_idx   = total_nof_elves-1

            continue

        curr_calories_cnt += int(line.strip())

print("\nThe highest number of calories currently being carried is %d\n" % (most_calories_val))
