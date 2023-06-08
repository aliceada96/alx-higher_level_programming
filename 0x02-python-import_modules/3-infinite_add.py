#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    adds = 0
    for i in range(len(sys.argv) - 1):
        adds += int(sys.argv[i + 1])
    print("{}".format(adds))
