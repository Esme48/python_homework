# Task 1
import logging

logging.basicConfig(level=logging.DEBUG)
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__ + "_parameter_log")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.FileHandler("./decorator.log", "a"))
        logger.info(f"function: {func.__name__}, positional parameters: {args}, keyword parameters: {kwargs}")
        #print(f"function: {func.__name__}, positional parameters")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger_decorator
def string_func():
    print("Hello, World!")

@logger_decorator
def positional_func(*args):
    #print(f"positional parameters: {args}")
    return True

@logger_decorator
def other_func(**kwargs):
    #print(f"keyword parameters: {kwargs}")
    return logger_decorator

string_func()
positional_func("Iris", 3)
other_func(name="bob", status="active", hobby="shopping")