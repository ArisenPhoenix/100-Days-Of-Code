import time


def time_to_run(function):
    def wrapper():
        start_time = time.time()
        data = function()
        end_time = time.time()
        elapsed_time = str(end_time - start_time)
        return f"{data}, {elapsed_time}"
    return wrapper


def to_header(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    
    return wrapper


def embolden(function):
    def wrapper():
        return f"<b>{function()}</b>"
    
    return wrapper
    

def italicize(function):
    def wrapper():
        return f"<i>{function()}</i>"
    
    return wrapper


def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    
    return wrapper


# def decorator(function):
#
#     def wrapper():
#         time.sleep(1)
#         function()
#
#     return wrapper
    
    


def say_hello():
    print("Hello")
    
    
def say_bye():
    print("Bye")
    