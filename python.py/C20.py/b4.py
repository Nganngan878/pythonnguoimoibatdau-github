#20/07/2026
"""
4.Asynchronous Functions
Task: Identify the two special keywords used to write and execute asynchronous code in Python based on the lesson notes.
Expected Output: async def (to define the function) and await (to wait for the result).

"""
import asyncio
async def down_file(file_name,delay):
    print(f"start down:{file_name}")
    await asyncio.sleep(delay)
    print(f"down done:{file_name}")
async def main():
    result=await asyncio.gather(
       down_file("video.map4",2),

       down_file("image.png",1))
    print("all down done:",result)
print("ready")