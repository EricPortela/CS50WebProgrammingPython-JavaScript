
#This is a so called decorator that takes a function and modifies it by adding some additional capabilities and returns an output 

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")

    return wrapper


#We add the decorator the the function "hello"
#In other words: We "wrap" the announce decorator around the hello-function
#A decorator can come in handy in a web application and in those cases you'd like to check those functions that you'd want to be run only when a user is logged in.
@announce
def hello():
    print("Hello world")


hello()