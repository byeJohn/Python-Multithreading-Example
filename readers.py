from time import sleep
from random import random
from threading import Thread
from threading import Lock
from threading import Semaphore
import random

m = Lock() #l1 in the example
# a custom function that blocks for a moment
read_count = 0
#An integer variable read_count is used to maintain the number of readers currently accessing the resource. The variable read_count is initialized to 0.
w = Semaphore(1)
#...and a semaphore w. A value of 1 is given initially to m and w.

def writers(tnum):
   while True:
      w.acquire()
      with m:
         print('Writer Entering: {}'.format(tnum))
         sleep(3)
      with m:
         print('Writers Exiting: {}'.format(tnum))
      w.release()
      

def readers(tnum):
   global read_count
   while True:
      #acquire lock
      m.acquire()
      read_count+= 1
      if read_count == 1:
         w.acquire()
      #release lock
      m.release()

      with m:
         print('Reader Entering: {}'.format(tnum))
      sleep(random.randint(3,5))
      with m:
         print('Reader Exiting: {}'.format(tnum))

      m.acquire()
      read_count-= 1
      if read_count == 0:
         w.release()

      m.release()

#taken from the threaded demo with modifications

thread = []
for i in range(3):
   #creates a thread
   thread.append(Thread(target=readers, args=(i,)))
   thread.append(Thread(target=writers, args=(i,)))
   # run the thread
   thread[i].start()
   # wait for the thread to finish

with m:
   print('Waiting for the threads to finish...')

for i in range(3):
   with m:
      print('Waiting for thread {} to finish...'.format(i))
   thread[i].join()
   with l1:
      print('Thread {} joined...'.format(i))

with m:
   print('Waiting done')


