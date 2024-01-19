import aiofiles
import asyncio
import datetime
import os
import sys

async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            await asyncio.sleep(0.001)
            data = await f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


async def main():
    begin = datetime.datetime.now()
    files = [os.path.join(root, file) for root, dirs, files in os.walk(sys.argv[1]) for file in files]
    tasks = [asyncio.create_task(read_file(file)) for file in files]
    for future in asyncio.as_completed(tasks):
        await future
    print(datetime.datetime.now() - begin)

asyncio.run(main())
