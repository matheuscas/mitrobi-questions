import asyncio

async def print_item_with_delay(item, delay):
    await asyncio.sleep(delay)
    print(item)

async def main():
    items = ["a", "b", "c", "d"]
    tasks = []
    delay = 1
    for item in items:
        tasks.append(asyncio.create_task(print_item_with_delay(item, delay)))
        delay *= 2
    await asyncio.gather(*tasks)

asyncio.run(main())
