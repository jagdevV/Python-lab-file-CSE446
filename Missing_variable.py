#Missing variable
# Full Program: Handling Missing Variable

def calculate_total():
    try:
        # Try using variable before defining
        print("Total value is:", total)
    except NameError:
        print("Variable 'total' is not defined.")
        print("Now defining the variable...")
        
        # Define the variable
        total = int(input("Enter a value for total: "))
        print("Total value is now:", total)

# Main Program
print("Program to Demonstrate Missing Variable Handling")
calculate_total()

print("Program executed successfully.")