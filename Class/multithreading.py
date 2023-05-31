# Multithreading.py
# import threading
# import time
# def worker():
#     counter = 0
#     while True:
#         time.sleep(1)
#         counter += 1
#         print(f": {counter}")

# threading.Thread(target=worker).start()

import threading
import time

def breakfast():
    print("I have breakfast")
    time.sleep(3)

def drink_coffee():
    print("I drank  coffee:")
    time.sleep(4)

def study():
    print("I am studying")    
    time.sleep(2)

x = threading.Thread(target= breakfast())   
y = threading.Thread(target= drink_coffee())   
z = threading.Thread(target= study())   


x.start()
y.start()
z.start()

x.join()
y.join()
z.join()

# breakfast()
# drink_coffee()
# study()
    


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter)
