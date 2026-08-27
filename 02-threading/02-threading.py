from threading import Thread
import time


def task(name,delay):
    print(f"starting task {name} with delay of {delay} seconds")
    time.sleep(delay)
    print(f"task {name} completed")
    

start = time.time()

thread1 = Thread(target=task,args=("A",2))
thread2 = Thread(target=task,args=("B",2))
thread3 = Thread(target=task,args=("C",2))

thread1.start()
thread2.start()
thread3.start()
print("All thread started")

thread1.join()
thread2.join()
thread3.join()

print("All threads finished")

end= time.time()

print(f"tasks completed in {end-start:.2f} seconds ")