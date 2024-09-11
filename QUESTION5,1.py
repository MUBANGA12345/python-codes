def print_args(*args, **kwargs):
    """
    Print out all the arguments received, clearly distinguishing between positional and keyword arguments.

    Args:
        *args: A variable number of positional arguments.
        **kwargs: A variable number of keyword arguments.
    """
    print("Positional Arguments:")
    for arg in args:
        print(f"- {arg}")
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"- {key} = {value}")

# Demonstrate the use of the function with various inputs
print_args(1, 2, 3, a=4, b=5)
print_args("hello", c=6, d=7)
print_args(x=8, y=9)
print_args(10, 11, 12)