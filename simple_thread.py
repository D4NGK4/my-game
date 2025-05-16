import threading
import time 

def a_function(number):
    print("Thread " + str(number) + ": starting")
    time.sleep(1)
    print("Thread " + str(number) + ": finished")
    
if __name__ == "__main__":
    threads = []
    
    for x in range(1,4):
        thread = threading.Thread(target=a_function, args=(x,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
    
    print("Program Completed")