
#This is a so called decorator that takes a function and modifies it by adding some additional capabilities and returns an output 

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")

    return wrapper


#We add the decorator the the function "hello"
#In other words: We "wrap" the announce function around the hello-function
@announce
def hello():
    print("Hello world")


hello()