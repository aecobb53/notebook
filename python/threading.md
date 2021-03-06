# Threading

## Links

# First video

## Types of computing

**Flynn's Taxonomy**
- SISD - Single Instruction Single Data
- SIMD - Single Instruction Multiple Data
- MISD - Multiple Instruction Single Data
- MIMD - Multiple Instruction Multiple Data

**Memory**
Shared memory
- UMA - Uniform Memory Access
    - SMP - Symetric Multiprocessing system
        - Has two or more identical processors that are connected to a single memory
- NUMA - Non-Uniform Memory Access
    - Usually made by connecting multiple UMA systems together
Shared memory processors are easier to program in because they share the memory but dont scale well

Distributed memory
- Connected through a network


## Threads and Processes

Talking between processes is harder than threads. 

To talk between processes you need to use things like: 
- IPC - Inter-Process Communication
    - Sockets and pipes
    - Shared memory
    - Remote procedure calls

If you can use threads its generally better. 
But between different computers you need multiple processes. 
There is less ohverhead to create and terminate a thread and an OS tends to switch ebtween threads faster than a proces.

**Concurrency** - The ability fo a program to be broken into parts that can run independently of each other. In order or out of order without effecting the end result. 

When making a salad, the first four steps are concurrent
```
Chop lettuce
Chopp cucumbers
Chop tomatoes
Chop onions
Add together for a salad
```

**Parallelism** is much like concurrency but if there are multiple processors it enables the concurrencys to occure simultaneously. 

Parallelism is great for complex math operations or things that take a while but can be run independantly. 
But most things are fine to run concurrently such as I/O operations. 

- GIL - Global Interpreter Lock. 
Prevents multiple python threads from executing at the same time. 
If you have 10 concurrent threads, onely 1 can execute at a time. 

`import threading` for multiple threads
`import multiprocessing` for multiple processors
If you are using multiple processors make sure to run an if statement to not spin up hundreds of unintended processes
```python
if '__name__' == '__main__':
    # suuf for spinning up different processes here
```

When creating threads they need to be told what to do. 
Sometimes they also require being told to start. 

Lifecycle of a thread `new`, `runable`, `blocked`, `terminated`. 
I dont think they all happen, but those are the four staets a thread can have. 

example lifecycle of a thread:
```python
class ChefOlivia(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        print('Olivia started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Olivia is done cutting sausage.')

# main thread
if __name__ == '__main__':
    print("Barron started & requesting Olivia's help.")
    olivia = ChefOlivia()
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron tells Olivia to start.')
    olivia.start()
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron continues cooking soup.')
    time.sleep(0.5)
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron patiently waits for Olivia to finish and join...')
    olivia.join()
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron and Olivia are both done!')
```
Notable events from the above script:
- olivia is created
- olivai.start() starts the process
- olivia.join() is used for the main thread to join olivia in the waiting que until olivia is done.
- Finally both process die as the have run their course
You can run `.is_alive()` to determin if a process is still alive. 
It will be false until it has been started and will return to false after it has exited. 
If the process is waiting it will still show as alive. 

**Garbage collector**

Automatic memory management. 
It reclaims memory no longer being used. 
If you set up a garbage collection thread it will never stop because there is always somethign to do. 
To get around this you need to _detatch_ aka create something called a `daemon thread`. 
_Note, theya re not limited to garbage collection_. 
To create a daemon thread use `.daemon = True` on the object. 
Daemon threads are abruptly terminated so make sure they arent doing anything that will cause issues if they are abruptly terminated. 
New threads will inherit the daemon status of the parent. 
You must set the daemon status before start or you will get a runtime error. 

## Locks

Data races occure if multiple threads are trying to access the same piece of data and at least one is trying to write to it. 

**Mutex**
`Mutex` (Lock) is a mutual exclusion event. 
Only one thread can have possetio of the lock at a time so its the only one that can update the resource. 
To create a data lock reference the following example. 
```python
pencil = threading.Lock()

def shopper():
    # somestuff
    pencil.acquire()
    # critical stuff
    pencil.release()
    # somestuff
```

**Reentrant Mutex**
Deadlock occures when a thread locks the resource and then tries to lock it again. 
Because its already locked the thread is incapable of locking it again and thus the system comes to a standstill. 
A `Reentrant Mutex` can be locked multiple times by the same process or thread. 
The number of lock events is kept track of and the same number must be unlocked before the resources is available again. 
A reentrant lock is set up by adding an `R` to the creation of a lock. 
```python
pencil = threading.RLock()
```
Another note of distinction between the two is a Lock can be released by a different thread but a RLock cannot. 

**TryLock**
`TryLock` will return `True` if the resource is not locked and `False` if it is. 
If you want the `.acquire()` method to return a bool add the `blocking=` parameter
```python
while True:
    if pencil.acquire(blocking=False):
        # somestuff
        pencil.release()
```
The code block above will only execute the `# somestuff` if lock was acquired, else it will continue through the loop. 

`Reader-Writer Lock` (shared Mutex) enables either `Shared Read` or `Exclusive Write`. 
Shared Read enables multiple threads that only need to read to lock it. 
Exclusive write mode limits the read/write to only one thread at a time. 
Reader-Writer Locks are not default in python. 
You will need to install `readerwriterlock` to use them
```python
from readwriterlock import rwlock

marker = rwlock.RLockFair()
```
`Fair` from the example above indicates it will give fair and even priority to readers/writers. 
`Read` or `Write` will give priority to readers or writers respectivly. 
To create the two specific locks you will need `gen_rlock()` and `gen_wlock()`. 
```python
from readwriterlock import rwlock

marker = rwlock.RLockFair()
# marker = rwlock.RLockRead()
# marker = rwlock.RLockWrite()

def cal_reader():
    read_marker.acquire()
    # reading only stuff
    read_marker.release()

def cal_write():
    write_marker.acquire()
    # Update only stuff
    write_marker.release()
```

## Liveness

If you need multiple locks like the dining philosophers problem, try to force each resource to acquire the same first lock. 
Using this example
```python
if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Olivia', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_c)).start()
```
and focusing on this section

'Barron', chopstick_`a`, chopstick_`b`)
'Olivia', chopstick_`b`, chopstick_`c`)
'Steve', chopstick_`a`, chopstick_`c`)

You can see that deadlock was avoided because the first letter in the alphabet was selected instead of the next in the trend. 
If Steve was to pick `chopstick_c` then `chopstic_a` we are likely to see deadlock. 

Another option is a timeout on the lock. 
A similar way to do this is a try loop
```python
lock.acquire()
try:
    # some stuff that may error
finally:
    lock.acquire()

# OR

with lock:
    # some stuff that may error
```

`Livelock` is similar to deadlock but both threads are starving themselvs trying to let the other go. 
The best way to get around deadlock and livelock at the same time are using `time` and `random`. 
```python
import threading
import time
from random import random

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0: # eat sushi until it's all gone
        first_chopstick.acquire()
        if not second_chopstick.acquire(blocking=False):
            print(name, 'released their first chopstick.')
            first_chopstick.release()
            time.sleep(random()/10)
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
            finally:
                second_chopstick.release()
                first_chopstick.release()

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Olivia', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Steve', chopstick_c, chopstick_a)).start()
```
In this example `time.sleep(random()/10)` is run if the 2nd chopstick was taken so the thread will wait a random amount of time and then try again. 
If scripts are dealing with deadlock they will not be using system resources but if they are sufferering from livelock they will be using full resources. 


# Seccond video

## Synchronization 

`Condition Variable` can be used as a que for the resource. 
`Monitor` can be used to protect a section of code and provide the ability for threads to wait until  a condition occures. 
The condition variable has three main operations: `wait`, `signal`, and `broadcast`. 
`wait` is what a thread will do while its waiting to use the resource. 
`signal` is what a thread does to a specific thread when its done with the resource. 
`broadcast` is what a thread will do to all waiting threads when its done with the resource. 
broadcast can be used for things like notifying when the queue is empty or not empty. 

Create a condition object to signal after someone has taken soup.
```python
import threading
slowcooker_lid = threading.Lock()
soup_taken = threading.Condition(Lock=slowcooker_lid)
```
The typical pattern is 
```python
lock.acquire()
while not (CONDITION):
    condition_variable.wait()

    # do something

lock.release()
```
Or using a context manager:
```python
with lock:
    while not (CONDITION):
        condition_variable.wait()
    # Do something
```
To add a notify do something like
```python
with lock:
    while not (CONDITION):
        condition_variable.wait()
    # Do something
    condition_variable.notify()
```
You can notify all threads waiting by switching `.notify()` to `.notify_all()`. 
If you dont care which thread is run next the regular notify works fine. 

---

**Producers** - Produce items for a queue

**Consumers** - Consume items from the queue

**queues**

| abbr | longhand |
| ---  | --- |
| FIFO | First-In-First-Out | 

**Pipeline** is the process items from a queue go through as they are processed. 

To create the maximum size of a queue use this
```python
import queue
serving_line = queue.Queue(maximize=5)
```
The `queue` module enables producers and consumers to access the queue without interfearing. 
To add items to the queue use `put_nowait` and to consume use `get`. 
```python
serving_line = queue.Queue(maximize=5)

def produce():
    serving_line.put_nowait('item')

def consume():
    bowl = serving_line.get()

```

# Multiprocessing
If the tasks are CPU restricting you can use multiple processors instead of threads. 
Because of the GIL, only 1 thead may be active at a time on a processor. 
You can increase the number of processors by using the `multiprocessing` module. 
You also need to pass the object into the functions for this one. 
The `maxsize-serving_line` as seen in `serving_line._maxsize-serving_line.qsize())` needs to have an `_` added after the object as seen in the second code block in this sentence. 
```python
import myltiprocessing as mp

serving_line = mc.Queue(5)

def soup_producer(serving_line):
    serving_line.put_nowait('item')

def soup_consumer(serving_line):
    bowl = serving_line.get()

if __name__ == '__main__':
    for consumer in range(2):
        mp.Process(target=soup_consumer, args=(serving_line,)).start()
    mp.Process(target=soup_producer, args=(serving_line,)).start()
```

**Semaphore** can be used by multiple threads at the same time. 
It includes a counter to track availability. 
If a counter is positive, the counter value is decremented when it is acquired. 
If the counter is zero the resource will wait until one is avilable. 
When you release a semaphore the waiting resources are notified. 

**Binary semaphore** is limited to either 1/0 resources. 
It looks a lot like a mutex. 
The difference is a mutex can only be released by the same resources that locked it. 
A semephore can be acquired/released by different threads. 
These can be used in a buffer. 
The producer decrements the empty count and increments the fill count. 
The consumer does the oposit and decrements the fill and increments the empty. 
This ensure the buffer never overflows or the opposite. 

To set a binary semephore initilize it with `1`. 
You can also use a context manager. 
```python
charger = threading.Semaphore(1)
with charger:
    # Do some stuff
```

# Barrier

**Data race** vs **Race condition**. 
A data race occures when two or more threads try to access and update the same location in memory at the same time and they interfear. 
Race condition is a flaw in order or timing in the program that causes improper behavior. 
Race conditions are sometimes called **Heisenbug**s. 
They are a software bug that disappears when you try to study it. 
Sometimes sleep statements are an alright way to get around these. 

A barrier is used to stop a run until all or enough threads have done their thing so you can proceed. 
The barrior can be used to syncronize events. 
Think PEMDAS from math, if a barrior is placed between each step, all parenthese math will be completed before the exponent math begins. 

To create a barrior do this. 
Notice how there are `10` threads that the barrier will wait for until releasing the threads again. 
You can add the barriers before or after steps but they will all occure at the same time. 
```python
fist_bump = threading.Barrier(10)

def barron_shopper():
    fist_bump.wait()
    # Stuff after wait

def olivia_shopper():
    # Stuff before the wait
    fist_bump.wait()
```

# Asynchronous tasks

`Spawn` will spawn asynchronous functions while `Sync` will bring them back together again. 
You will also see `Fork` and `Join` used in the same context. 

DAG = Directed Acyclic Graph. 
This was the image used in the video to show that the second thread could take one of the async processies while the main thread took the other. 

`Work` indicates the total work done by the program. 
The `Critical Path` is the path of most work if everything was parallelerized as much as possible. 
This is important because if work was time the critical path would indicate the shortest amount of time anything could get through because everything would need to wait for the critical path in the end anyway. 
`Span` is the amount of work in the critical path. 
The `Ideal Parallelism` ration is the `work`/`sman` and is a positive fraction or float. 
For example if the Work for a program is 60 and the Span is 45, the Ideal Parallelism is 60/45 or 1.33. 
This means the the parallelism is 33% faster than running everything in sequential order. 

Because spawning many async threads can get crouded and chaotic you can use `Thread Pool`s. 
They create and maintain a collection of workers. 
When a task is submitted the pool will re-use threads when they are available. 




























