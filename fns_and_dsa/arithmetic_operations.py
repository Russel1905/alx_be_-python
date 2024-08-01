def perform_operation(num1, num2, operation):
    """
    This function performs basic arithmetic operations.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - The result of the operation, or a message in case of division by zero.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
