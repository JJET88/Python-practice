import threading

def my_function(arg1, arg2):
    # code to be executed in the new thread
    print("Thread started with arguments:", arg1, arg2)

# create a new thread with arguments
t = threading.Thread(target=my_function, args=("arg1_value", "arg2_value"))

# start the new thread
t.start()

# wait for the thread to finish
t.join()

print("Thread finished")

print("")