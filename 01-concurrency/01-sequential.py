import time 

def task(name):
    print(f"Starting Task {name}")
    time.sleep(2)
    print(f"Ending task {name}")
    
start = time.time()

task("A")
task("B")
task("C")

end = time.time()

print(f"Total time :{end-start:.2f} seconds")