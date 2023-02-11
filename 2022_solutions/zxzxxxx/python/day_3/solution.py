test = "vJrwpWtwJgWrhcsFMMfFFhFp"
len_str = len(test)

if len_str % 2 == 0:
    str1 = test[0:len_str//2]
    str2 = test[len_str//2:]
    print(str1)
    print(str2)