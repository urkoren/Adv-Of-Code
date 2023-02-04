PAIR_SEPERATOR  = ','
RANGE_SEPERATOR = '-'
INPUT_FILENAME  = 'input.txt'

def get_range_pair_from_line(line: str) -> tuple[str, str]:
    global PAIR_SEPERATOR

    return line.strip().split(PAIR_SEPERATOR)

def get_range_min_max(range: str) -> tuple[min: int, max: int]:
    global RANGE_SEPERATOR
    min_str, max_str = range.split(RANGE_SEPERATOR)
    return int(min_str), int(max_str)

def has_sub_set(r1: str, r2: str) -> bool:
    r1_min, r1_max  = get_range_min_max(r1)
    r2_min, r2_max  = get_range_min_max(r2)

    if (r1_min<=r2_min and r1_max>=r2_max):
        return True
    if(r2_min<=r1_min and r2_max>=r1_max):
        return True

    return False

def shares_a_member(r1: str, r2: str) -> bool:
    r1_min, r1_max  = get_range_min_max(r1)
    r2_min, r2_max  = get_range_min_max(r2)

    if (r1_min>=r2_min and r1_min<=r2_max):
        return True
    if(r1_max>=r2_min and r1_max<=r2_max):
        return True
    if (r2_min>=r1_min and r2_min<=r1_max):
        return True
    if(r2_max>=r1_min and r2_max<=r1_max):
        return True
        

    return False

def part_one_solution() -> int:
    global INPUT_FILENAME

    subset_count = 0

    with open(INPUT_FILENAME, 'r') as file:
        for line in file:
            r1, r2 = get_range_pair_from_line(line)
            subset_count += int(has_sub_set(r1, r2))

    return subset_count

def part_two_solution() -> int:
    global INPUT_FILENAME

    solution = 0

    with open(INPUT_FILENAME, 'r') as file:
        for line in file:
            r1, r2      = get_range_pair_from_line(line)
            solution    += int(shares_a_member(r1, r2))

    return solution

def main():
    p1_solution = part_one_solution()
    p2_solution = part_two_solution()

    print(f'Number of subset pairs is: {p1_solution}')
    print(f'Number of pairs that share at least one member: {p2_solution}')

if __name__ == '__main__':
    main()
