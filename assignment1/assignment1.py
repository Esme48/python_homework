#Task 1

def hello():
    return "Hello!"

#Task 2

def greet(name):
    return f"Hello, {name}!"

print(greet("Henry"))

#Task 3

def calc(x,y, operation="multiply"):
    if operation == "add":
        return x+y
    elif operation == "subtract":
        return x-y
    elif operation == "multiply":
        try:
            return x*y
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "divide":
        try: 
            return x/y
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "modulo":
        return x%y
    elif operation == "int_divide":
        return x//y
    elif operation == "power":
        return x**y
    
print(calc(1,5, "divide"))

#Task 4

def data_type_conversion(value, name="int"):
    try:
        if name == "int":
            return int(value)
        elif name == "float":
            return float(value)
        elif name == "str":
            return str(value)
    except Exception as e:
        return f"You can't convert {value} into a {name}."

#Task 5

def grade(*args):
    try:
        if len(args) == 0:
            return "Invalid data was provided."
        
        avg = sum(args)/len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except Exception as e:
        return "Invalid data was provided."
    
#Task 6: 

def repeat(string, count):
    return string*count

#Task 7:  

def student_scores(value, **kwargs):
    if value == "best":
        best = max(kwargs, key = kwargs.get)
        return best
    elif value == "mean":
        average = sum(kwargs.values())/len(kwargs)
        return average
    
#Task 8:

def titleize(string):
    small_values = ["a", "on", "an", "the", "of", "and", "is", "in"]
    new_string = string.split()

    for i, word in enumerate(new_string):
        if i == 0 or i == len(new_string) - 1 or word.lower() not in small_values:
            new_string[i] = word.capitalize()
        else:
            new_string[i] = word.lower()
    
    return " ".join(new_string)


print(titleize("Welcome to my kitchen"))

# Task 9:

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


print(hangman("Thank you for coming", "aing"))

