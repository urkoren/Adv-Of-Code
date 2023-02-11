from dataclasses import dataclass

input_file = "input.txt"

@dataclass(init=False)
class ElfInfo:
    nof_top_cal_elves       : int   
    top_cal_elves           : list[int]
    found_first_elf_flag    : bool
    current_sum             : int
    
    def __init__(self, nof_top_cal_elves : int) -> None:
        self.nof_top_cal_elves      = nof_top_cal_elves
        self.top_cal_elves          = [0 for elf in range(nof_top_cal_elves)]
        self.found_first_elf_flag   = False
        self.current_sum            = 0


    def is_new_elf(self, line : str) -> bool:
        if line == "":
            return False

        if not self.found_first_elf_flag and line.strip().isnumeric():
            return True

        if line.isspace():
            return True

        return False


    def add_to_current_sum(self, line : str) -> bool:
        if not line.strip().isnumeric():
            return False

        self.current_sum += int(line)
        return True
    

    def update_top_cals(self) -> None:
        for i in range(len(self.top_cal_elves)):
            if self.current_sum > self.top_cal_elves[i]:
                self.top_cal_elves[i] = self.current_sum
                self.top_cal_elves.sort() 
                break
        
        
          

def solution_1():
    elf_info = ElfInfo(1)
    
    with open(input_file, "r") as file:
        for line in file:
            if elf_info.found_first_elf_flag and elf_info.is_new_elf(line):
                elf_info.update_top_cals()
                elf_info.current_sum = 0
                continue   
            
            if elf_info.add_to_current_sum(line):
                elf_info.found_first_elf_flag = True
             
    print(sum(elf_info.top_cal_elves))
    
def solution_2():
    elf_info = ElfInfo(3)
    
    with open(input_file, "r") as file:
        for line in file:
            if elf_info.found_first_elf_flag and elf_info.is_new_elf(line):
                elf_info.update_top_cals()
                elf_info.current_sum = 0
                continue   
            
            if elf_info.add_to_current_sum(line):
                elf_info.found_first_elf_flag = True
             
    print(sum(elf_info.top_cal_elves))
    
if __name__ == "__main__":
    solution_1()
    solution_2()
    