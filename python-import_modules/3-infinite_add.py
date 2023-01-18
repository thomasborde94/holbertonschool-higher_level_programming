#!/usr/bin/python3
import sys
def infinite_add():
    if __name__ == "__main__":
        result = 0
        if len(sys.argv) == 1:
            print("0")
        else:
            for i in range(1, len(sys.argv)):
                result += int(sys.argv[i])
                i += 1
                print("{}".format(result))

infinite_add()
