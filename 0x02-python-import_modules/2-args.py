#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_total = len(sys.argv)
    if arg_total <= 1:
        print("0 arguments.")
    else:
        if arg_total == 2:
            print("{:d} argument:".format(arg_total - 1))
        else:
            print("{:d} arguments:".format(arg_total - 1))
        for i in range(1, arg_total):
            print("{:d}: {}".format(i, sys.argv[i]))
