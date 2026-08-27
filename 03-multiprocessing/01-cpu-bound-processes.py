from multiprocessing import Process
import time

def cpu_heavy(name,limit):
    start = time.time()
    total = 0
    for num in range(limit):
        total = total + (num*num)
    end = time.time()
    print(f"executed {name} in {end-start:.2f} seconds")
    return total


if __name__ == "__main__":
    start=time.time()
    process1 = Process(target=cpu_heavy,args=("A",100_000_000))
    process2 = Process(target=cpu_heavy,args=("B",100_000_000))
    process3 = Process(target=cpu_heavy,args=("C",100_000_000))
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()
    print(f"total time taken {time.time()-start:.2f} seconds")