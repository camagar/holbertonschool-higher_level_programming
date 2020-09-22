def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            print()
        except IndexError:
            print()
            return i
    return x
