# Example 1-2
# vs Synchrous Thread
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
    say1()
    say2()
    write("exit")
