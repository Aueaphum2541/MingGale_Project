import asyncio

def write(msg):
    print(msg, flush=True)

async def say1():
    await asyncio.sleep(1)
    write("Hello 1!")

async def say2():
    await asyncio.sleep(1)
    write("Hello 2!")

async def main():
    await asyncio.gather(say1(), say2())
    
if __name__ == "__main__":
    import time
    write("start")
    s = time.perf_counter()
    asyncio.run(main())
    print("exit")
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.") 
    
# write("start")
# loop = asyncio.new_event_loop()  # Create a new event loop
# asyncio.set_event_loop(loop)     # Set the new event loop
# loop.run_until_complete(asyncio.gather(say1(), say2())) 
# write("exit")

# loop.close() 
