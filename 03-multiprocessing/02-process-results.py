from multiprocessing import Process,Queue
import time


def cpu_heavy(name,limit,result):
    start = time.time()
    total = 0
    for num in range(limit):
        total = total + (num*num)
    end = time.time()
    print(f"executed {name} in {end-start:.2f} seconds")
    result.put((name,total))

if __name__ == "__main__":
    result = Queue()
    p1 = Process(target=cpu_heavy,args=("A",100_000_000,result))
    p2 = Process(target=cpu_heavy,args=("B",100_000_000,result))
    p3 = Process(target=cpu_heavy,args=("C",100_000_000,result))
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()
    print(result.get())
    print(result.get())
    print(result.get())
    print(f"completed in {end-start:.2f} seconds")
