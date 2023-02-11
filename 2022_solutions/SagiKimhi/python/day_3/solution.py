INPUT_FILENAME = 'input.txt'

def slice_string_to_half(s: str) -> tuple[str, str]:
    s_len = len(s)

    if (s_len<=1):
        return s
    return s[0:(s_len//2)], s[(s_len//2):]

def convert_chr_to_priority_val(c: chr) -> int:
    NUM_LETTERS_IN_ALPHABET = ord('z')-ord('a')+1
    UPPER_SUB_VAL           = ord('A')-1-NUM_LETTERS_IN_ALPHABET
    LOWER_SUB_VAL           = ord('a')-1

    if str(c).isupper():
        return ord(c)-UPPER_SUB_VAL
    
    return ord(c)-LOWER_SUB_VAL

def convert_str_to_priority_val_sum(s: str) -> int:
    res = 0

    for c in s:
        res += convert_chr_to_priority_val(c)

    return res

def find_duplicate_chars_from_s1_in_s2(s1: str, s2: str) -> str:
    res = ''
    s1_chr_dict = {c:0 for c in s1}

    for c in s2:
        if (s1_chr_dict.pop(c, 1)!=1):
            res += c

    return res

def find_duplicate_char_in_n_strings(s_list: list[str]) -> str:
    duplicates = ''

    for s in s_list:
        if (duplicates==''):
            duplicates = s
            continue

        duplicates = find_duplicate_chars_from_s1_in_s2(duplicates, s)
    
    return duplicates

def part_1_solution() -> int:
    solution = 0

    with open(INPUT_FILENAME, 'r') as file:
        for line in file:
            s1, s2 = slice_string_to_half(line)
            solution += convert_chr_to_priority_val(find_duplicate_chars_from_s1_in_s2(s1, s2))

    return solution

def part_2_solution():
    NUM_ELF_GROUPS  = 3
    solution        = 0

    with open(INPUT_FILENAME, 'r') as file:
        while True:
            try:
                lines       = [next(file).strip() for i in range(NUM_ELF_GROUPS)]
                solution    += convert_chr_to_priority_val(find_duplicate_char_in_n_strings(lines))
            except:
                break
    
    return solution


def main():
    solution1 = part_1_solution()
    solution2 = part_2_solution()
    print(f'sum of priorities of item type duplicates is: {solution1}')
    print(f'sum of priorities of item type badges is: {solution2}')

if __name__ == '__main__':
    main()
