# Fibonacci Series Project


# Function to calculate a Fibonacci number
def fibonacci(n):


    # First Fibonacci number
    if n == 0:
        return 0


    # Second Fibonacci number
    elif n == 1:
        return 1


    # Add the previous two Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)




# Ask the user how many terms they want
terms = int(input("Enter the number of terms: "))




# Check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive number.")


else:


    # Print the Fibonacci sequence
    print("Fibonacci Series:")


    for i in range(terms):
        print(fibonacci(i), end=" ")