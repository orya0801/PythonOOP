from time import sleep
import random
import time
import asyncio


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print("{} waited {} seconds""".format(name, time_to_sleep))


"""
обе сопрограммы завершат свое выполнение, но не асинхронно

для асинхронного завершения нужно использовать asyncio.sleep(),
которая является асинхронной версией time.sleep(),
и ожидать результата с помощью ключевого слова await
"""


async def main():
    await asyncio.wait([waiter("foo"), waiter("bar")])


if __name__ == "__main__":
    asyncio.run(main())  # Python 7+
