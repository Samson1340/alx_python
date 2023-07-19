def fibonacci_sequence(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)
 
# Driver Program
 
print(fibonacci_sequence(5))