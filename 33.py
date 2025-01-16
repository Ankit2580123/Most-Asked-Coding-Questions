#Use threading modules to show concurrent execution of thread at a same time 
#Thread is a segment of process
#Process is a Program in execution

import time
import threading
def sleeping(seconds):
    time.sleep(seconds)
    print(f"Sleeping Time {seconds} seconds")

#Normal 
time1=time.perf_counter()
# sleeping(2)
# sleeping(1)
# sleeping(2)
# time2=time.perf_counter()

#using Threads

t1=threading.Thread(target=sleeping,args=[2])
t2=threading.Thread(target=sleeping,args=[1])
t3=threading.Thread(target=sleeping,args=[2])

t1.start() #Start the thread's activity.
t2.start()
t3.start()

t1.join()  #Wait until the thread terminates.
t2.join()
t3.join()

time2=time.perf_counter()
print(f"Total Time Taken to Executes: {round(time2-time1)} seconds")




    

