/**
    Java API java.util.concurrent

    process
    - has a self-contained execution environment including memory space
    - IPC - pipes and sockets handle byte streams
        - pipes - communication on same host, buffering b/w virtual files, no
        packets
        - sockets - use IPv4 or IPv6 and packetize messages, can communicate
        beyond localhost,
        endpoints can share IP and differ by port
    - Most JVMs single process, create more with `ProcessBuilder` object.

    threads
    - lightweight process, exist within a process; shares the process's resources
    including memory and open files

    Thread
    - create your own Thread for each asynchronous task
    - pass tasks to executor
*/

// Runnable
public class HelloRunnable implements Runnable {
    public void run(){
        // run
    }
    public static void main(String[] args){
        (new Thread(new HelloRunnable())).start();
    }
}

// Thread.sleep()
public class SleepMessages {
    public static void main(String[] args) throws InterruptedException {
        String[] info = {"a", "b", "c", "d"};
        for (String s: info){
            Thread.sleep(4000);
            System.out.println(s);
        }
    }
}

// Interrupts
for (int i = 0; i < inputs.length; i++) {
    heavyCrunch(inputs[i]);
    if (Thread.interrupted()){
        return
        // OR throw new InterruptedException();
    }
}

// Join
// current thread pauses until t's thread terminates
try{
    t.join()
}catch(InterruptedException e){

}


// Synchronization
Helps:
- thread interference
- memory consistence errors

Introduces: thread contention including starvation and livelock

Interference - happens when two operations, running in different threads, but acting
on the same data, interleave.

Memory consistency errors - different threads have inconsistent views of what
should be the same data. Avoid by using happens-before relationship, which
guarantees that memory writes by one specific statement are visible to another
specific statement.

Synchronized methods establish happens-before but hamper liveness.


// Intrinsic Locks and Synchronization
- synchronization build around intrinsic or monitor locks (monitor)
- every Java object has one

public void addName(String n) {
    synchronized(this) {
        lastName = name;
        nameCount++;
    }
    nameList.add(name)
}


// Atomic Access

- read and writes are atomic for reference variable and for most primitive
variables (except long and double)
- read and writes are atomic for all variables declared volatile
(including long and double variables)

- using 'volatile' variables reduces the risk of memory consistency errrors,
because any write to a volatile variable establishes a happens-before relationship
with subsequent read of that same variable. Changes to a volatile variable are
always visible to other threads.

- using simple atomic variable access more efficient than accessing these
variables through synchronized code, but requires more care by the programmer
to avoid memory consistency errors

// Immutable objects
An object is considered immutable if its state cannot change after it is
constructed. Maximum reliance on immutable objects is widely accepted as a
sound strategy for creating simple, reliable code.

Immutable objects are particularly useful in concurrent applications. Since
they cannot change state, they cannot be corrupted by thread interference or
observed in an inconsistent state.

// Locks
The biggest advantage of Lock objects over implicit locks is their ability to
back out of an attempt to acquire a lock. The tryLock method backs out if the
lock is not available immediately or before a timeout expires (if specified).
The lockInterruptibly method backs out if another thread sends an interrupt
before the lock is acquired.
 // TODO code example

// Executor interface
The ExecutorService interface supplements execute with a similar, but more
 versatile submit method. Like execute, submit accepts Runnable objects, but
 also accepts Callable objects, which allow the task to return a value. The
 submit method returns a Future object, which is used to retrieve the Callable
 return value and to manage the status of both Callable and Runnable tasks.

// thread pools
executors use them
graceful degradation
java.util.concurrent.ThreadPoolExecutor or java.util.concurrent.ScheduledThreadPoolExecutor


// Fork / Join
The first step for using the fork/join framework is to write code that performs
a segment of the work. Your code should look similar to the following pseudocode:
if (my portion of the work is small enough)
  do the work directly
else
  split my work into two pieces
  invoke the two pieces and wait for the results


// Concurrent collections
BlockingQueue - FIFO q that blocks or times out when add to full or retrieve empty
ConcurrentHashMap
ConcurrentNavigableMap - supports approximate matches

// Atomic Variables
e.g., AtomicInteger #incrementAndGet() #decrementAndGet()













