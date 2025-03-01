import streamlit as st

def calculator():
    st.title("Simple Calculator using Streamlit")
    
    # User input for numbers
    num1 = st.number_input("Enter first number", value=0.0, format="%f")
    num2 = st.number_input("Enter second number", value=0.0, format="%f")
    
    # Select operation
    operation = st.radio("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))
    
    # Perform calculation
    result = None
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero is not allowed")
    
    # Display result
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    calculator()