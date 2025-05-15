import threading
import time 

def a_function(number):
    print("Thread " + str(number) + ": starting")
    time.sleep(1)
    print("Thread " + str(number) + ": finished")
    
if __name__ == "__main__":
    t1 = threading.Thread(target=a_function, args=(1,))
    t2 = threading.Thread(target=a_function, args=(2,))
    t3 = threading.Thread(target=a_function, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    
    print("Program Completed")