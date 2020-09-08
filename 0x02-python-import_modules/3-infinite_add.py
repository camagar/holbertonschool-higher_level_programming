#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Nargs = len(sys.argv)
    suma = 0
    if Nargs > 1:
        for i in range(1, Nargs):
            aux = int(sys.argv[i])
            suma += aux
        print("{:d}".format(suma))
    else:
        print("{}".format(0))
