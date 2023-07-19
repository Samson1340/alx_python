for x in range(100):
    if x <= 9:
        print("0{},".format(x))
    elif x == 99:
        print("{}".format(x))
    else:
        print("{}, ".format(x))