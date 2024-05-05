import asyncio
import curses
import math

total_distance = 100

class RaceFinishedException(Exception):
    ...

async def achilles(stdscr):
    achilles_position = 0
    achilles_speed = 10
    positions = ["-"] * total_distance
    positions[achilles_position] = "A"
    while achilles_position < total_distance:
        stdscr.addstr(0, 0, f"Achilles position is {achilles_position}")
        stdscr.addstr(1, 0, "".join(positions))
        stdscr.refresh()
        achilles_position += achilles_speed
        achilles_speed /= 2
        positions = ["-" for _ in positions]
        positions[min(math.ceil(achilles_position), total_distance - 1)] = "A"
        await asyncio.sleep(0.5)


async def tortoise(stdscr):
    tortoise_speed = 5
    tortoise_position = 20
    positions = ["-"] * total_distance
    positions[tortoise_position] = "T"
    while tortoise_position <= total_distance:
        stdscr.addstr(2, 0, f"Tortoise position is {tortoise_position}")
        stdscr.addstr(3, 0, "".join(positions))
        stdscr.refresh()
        tortoise_position += tortoise_speed
        positions = ["-" for _ in positions]
        positions[min(math.ceil(tortoise_position), total_distance - 1)] = "T"
        await asyncio.sleep(1)
    raise RaceFinishedException()


async def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()  # Clear the screen

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(achilles(stdscr))
            tg.create_task(tortoise(stdscr))
    except* Exception:
        stdscr.addstr(4, 0, "Race has finished")
        stdscr.refresh()

def sync_main():
    asyncio.run(main(curses.initscr()))

sync_main()
