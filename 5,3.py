import time
import functools

def timer_decorator(func):
    """
    A decorator function that measures and prints the execution time of any function it decorates.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# Example usage:
@timer_decorator
def sort_large_list():
    """
    A function that performs a time-consuming task: sorting a large list.
    """
    large_list = [i for i in range(10000)]
    sorted_list = sorted(large_list)
    return sorted_list

# Call the decorated function
sort_large_list()