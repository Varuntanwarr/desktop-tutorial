# Function to add two numbers
def add(v, s):
    return v + s

# Function to subtract two numbers
def subtract(v, s):
    return v - s

# Function to multiply two numbers
def multiply(v, s):
    return v * s

# Function to divide two numbers
def divide(v, s):
    if s == 0:
        return "Cannot divide by zero!"
    else:
        return v / s

# Main function
def main():
    print("welcome to cui calculator app")
    while True:
        print("\nOperations:")
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            varun1 = float(input("Enter first number: "))
            varun2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(varun1, varun2))
            elif choice == '2':
                print("Result:", subtract(varun1, varun2))
            elif choice == '3':
                print("Result:", multiply(varun1, varun2))
            elif choice == '4':
                print("Result:", divide(varun1, varun2))
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
