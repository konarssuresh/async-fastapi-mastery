import time 
from threading import Thread


def cpu_heavy(name,limit):
    start = time.time()
    total = 0
    for num in range(limit):
        total = total + (num*num)
    end = time.time()
    print(f"executed {name} in {end-start:.2f} seconds")
    return total

start=time.time()
# cpu_heavy("A",100_000_000)
# cpu_heavy("B",100_000_000)
# cpu_heavy("C",100_000_000)

thread1 = Thread(target=cpu_heavy,args=("a",100_000_000))
thread2 = Thread(target=cpu_heavy,args=("b",100_000_000))
thread3 = Thread(target=cpu_heavy,args=("c",100_000_000))
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

end= time.time()

print(f"Completed main thread execution in {end-start:.2f} seconds")