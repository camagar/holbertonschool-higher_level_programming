#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    largs = sys.argv
    if nargs == 1:
        print("{} arguments.".format(nargs - 1))
    elif nargs == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(1, nargs):
        print("{}: {}".format(i, largs[i]))
