# Adapted from: SuperFastPython.com
# example of running a function in another thread
from time import sleep
from threading import Thread
from threading import Lock
 
l1 = Lock()
# a custom function that blocks for a moment
def task(tnum):
    # block for a moment
    with l1:
       print('Starting thread: {}'.format(tnum))
    sleep(5-tnum)
    # display a message
    with l1:
       print('Leaving thread: {}'.format(tnum))
 
thread = []
for i in range(3):
   # create a thread
   thread.append(Thread(target=task,args=(i,)))
   # run the thread
   thread[i].start()
   # wait for the thread to finish

with l1:
   print('Waiting for the threads to finish...')

for i in range(3):
   with l1:
      print('Waiting for thread {} to finish...'.format(i))
   thread[i].join()
   with l1:
      print('Thread {} joined...'.format(i))

with l1:
   print('Waiting done')

