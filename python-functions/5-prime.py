def is_prime(number):
    is_prime = True
    if number == 1:
        is_prime = False
    elif number > 1:
        for x in range(2,int(number/2)+1):
            if number % x == 0:
                is_prime = False
            else:
                is_prime = True
    return is_prime