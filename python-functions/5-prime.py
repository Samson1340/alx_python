def is_prime(number):
    is_prime = True
    if number == 1 | number <= 0:
        is_prime = False
    elif number > 1:
        for x in range(2,number):
            if number % x == 0:
                is_prime = False
    return is_prime