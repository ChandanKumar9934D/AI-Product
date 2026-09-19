# 1. Ask for the operator first
sign = input("Enter the sign that you want to calculate (+, -, *, /): ")

def getnumber():
    firstNumber = float(input("Enter the first Value: "))
    secondNumber = float(input("Enter the second Value: "))
    return [firstNumber, secondNumber]

def calculate():
    getValu = getnumber()
    
    # 2. Check the sign and perform the correct calculation
    if sign == '+':
        result = getValu[0] + getValu[1]
    elif sign == '-':
        result = getValu[0] - getValu[1]
    elif sign == '*':
        result = getValu[0] * getValu[1]
    elif sign == '/':
        # Optional: Add a check to prevent division by zero
        if getValu[1] == 0:
            return print("Error: Cannot divide by zero!")
        result = getValu[0] / getValu[1]
    else:
        return print("Invalid operator entered.")
        
    print(f"Result: {result}")

# 3. Call the function to start the calculator
calculate()
