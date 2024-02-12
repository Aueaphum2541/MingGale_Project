# Example 1-3
# multithreading
import threading
import time

def write(msg):
    print(msg, flush=True)  # flush=True is needed to ensure the message is printed immediately

def say1():
    time.sleep(1)
    write("Hello 1!")

def say2():
    time.sleep(1)
    write("Hello 2!")

if __name__ == "__main__":
    write("start")
    
    # Create and start threads for say1 and say2 functions
    thread1 = threading.Thread(target=say1)
    thread2 = threading.Thread(target=say2)
    thread1.start()
    thread2.start()
    
    
    # Wait for both threads to finish execution
    thread1.join()
    thread2.join()

    write("exit")
