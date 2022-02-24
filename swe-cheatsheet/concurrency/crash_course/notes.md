Threads give illusion of multitasking even though CPU is 
executing 1 at any point in time.

Multicore machines can have a dedicated core run each thread, however
 Python is limite by GIL.

Networking and disk I/O can see significant performance gains

Process
- program in exeuction, instructions, user data, system data, CPU, memory, address space, disk, network I/O

Thread
- smallest unit of execution in a process. has thread-private state but also can access process-shared state
- shared state is guarded by various programming constructs

Concurrency
- doing multiple things at once using time sharing

Parallelism
- doing multiple things at once by using multiple workers

Preemptive multitasking
- OS scheduler determines thread/program to run next and for how long, not programmer / program

Cooperative multitasking
- programs voluntarily give up control back to scheduler

Throughput (concurrency)
- time taken to execute a computation, e.g. files processed per minute

Latency
- time required to complete a task, e.g. time to complete process all files

Synchronous execution
- line-by-line execution, serial

Asynchronous execution
- execution that doesn't block when invoking subroutines
- subroutine returns future/promise or a callback function is passed to the asynch function call
- good for network or disk I/O

CPU bound
- programs whose execution requires very high CPU utilization
- data crunching, image processing, matrix multiplication

I/O bound
- programs whose execution spends most of their time waiting for input/output operations to complete while CPU is idel

Thread safety
- immutable state
- shared state mutated by atomic bytecode instruction, can be safely read by multiple readers
- guarding shared data with mutex or lock

Critical section
- code that can be executed concurrently by more than one thread of the application
- code that exposes any shared data or resources used by the application

Race condition
- when threads run through critical sections without thread synchronization

Deadlock
- two or more threads are stuck b/c each are holding locks required by the other

Liveness
- ability to execute in a timely manner

Live-lock
- threads reacting to each other without making any real progress

Starvation
- thread doesn't get CPU time or access to shared resources

Reentrant lock
- lock that allows reentry by a thread already holding the lock

Mutex
- guards shared data allowing onle a single thread to access a critical section
- other threads are blocked until the first thread release

Semaphore
- limits access to a collection of resources, has a limited number of permits, e.g. pool of db connections
- binary semaphore = single permit != mutex
- can be used to signal among threads

binary semaphore vs mutex
- mutex: same thread must acquire and release; binary semaphore: different threads can acquire and release
- mutex is owned by acquiring thread until release; semaphore has no ownership

Condition variables
- object with wait and notify/signal methdos
- wait() > caller sent to wait queue

Monitor
- mutex and one or more condition variables
- predicate always tested in a while loop
- Python "Condition" which implicitly has a lock or may be passed one
- mutex with a wait set and entry set
- allows threads to exercise mutual exclusion as well as cooperation 
- threads enter the entry set, then one may enter the monitor, they may then wait in the wait set OR
they may leave the monitor after signaling
- python monitors are Hoare monitors which requires checking for condition in a while loop
- language-level construct (mutex, semaphore lower level)
- prepacked solution, less error prone than semaphore, but semaphores are more lightweight

GIL
- execution of Python bytecode requires acquiring a single lock providing exclusive access to python interpreter
- could have had 1 lock per object, however it would be hard to avoid deadlocks
- threads in Python are only good for blocking I/O

Amdahl's law
- n = threads, P = fraction of program parallelizable, S = speedup
- S(n) = 1 / [(1-P) + P/n]

Daemon Thread
- runs in the background, program may exit if the daemon thread is still not finished, but python program
will wait for non-daemon
- daemons are shut down abruptly so open resources would not be closed properly
