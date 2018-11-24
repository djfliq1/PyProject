import csv
import datetime
import time
import sys
import asyncio

async def mytest():
    while True:
        await asyncio.sleep(1)
        print('someShit')

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(mytest())
    loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    loop.close()
