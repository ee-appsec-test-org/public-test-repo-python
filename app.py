#!/usr/bin/env python3
"""
A simple dummy Python application.
"""


def greet(name="World"):
    """
    Returns a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """
    Main function to run the application.
    """
    print(greet())
    print(greet("Python Developer"))
    
    # Get user input
    user_name = input("Enter your name: ")
    if user_name:
        print(greet(user_name))


if __name__ == "__main__":
    main()
