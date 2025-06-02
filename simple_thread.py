import threading
import time
from typing import List

def execute_task(thread_id: int) -> None:
    print(f"Thread {thread_id}: starting")
    time.sleep(1)
    print(f"Thread {thread_id}: finished")

if __name__ == "__main__":
    active_threads: List[threading.Thread] = []
    
    for thread_id in range(1, 4):
        worker = threading.Thread(target=execute_task, args=(thread_id,))
        active_threads.append(worker)
        worker.start()
    
    for worker in active_threads:
        worker.join()
    
    print("Program Completed")