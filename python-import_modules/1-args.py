if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1

    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))

    if num >= 1:
        num = 0
        for arg in sys.argv:
            if num != 0:
                print("{}: {}".format(num, arg))
            num += 1