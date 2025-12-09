# Task 1
import logging

logging.basicConfig(level=logging.DEBUG)
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__ + "_parameter_log")
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.FileHandler("./decorator.log", "a"))
        print(f"function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger_decorator
def string_func():
    print("Hello, World!")

def positional_func(*args):
    print(f"positional parameters: {args}")
    return True

def other_func(**kwargs):
    print(f"keyword parameters: {kwargs}")
    return logger_decorator

string_func()
positional_func("Iris", 3)
other_func(name="bob", status="active", hobby="shopping")