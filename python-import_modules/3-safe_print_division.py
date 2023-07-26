def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        print("{} / {} = None".format(a, b))
    finally:
        print("Inside result: {}".format(c))
        print("{} / {} = {}".format(a, b, c))
