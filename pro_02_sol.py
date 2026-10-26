def inch_to_cm(inch):
    """
    Convert inches to centimeters.
    
 Parameters:
    inch (float): The value in inches to be converted.
    
    Returns:
    float: The value in centimeters.
    """
    return inch * 2.54
n = float(input("Enter the value in inches: "))
cm = inch_to_cm(n)  
print(f"{n} inches is equal to {cm} centimeters.")
# The code above defines a function to convert inches to centimeters and then uses it to convert a user-provided value.