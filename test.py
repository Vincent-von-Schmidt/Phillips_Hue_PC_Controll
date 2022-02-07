import requests
import json
import asyncio
import httpx


async def request_sim(request: bool = False) -> None:
    print("request start")

    if request:

        async with httpx.AsyncClient() as client:
            content = await asyncio.gather(
                client.get(
                    url="http://192.168.178.37/api/UoghabPi6o43qbmxud5U76fjgKF6BPtgznFCM-FT/lights/3/"
                )
            )

        print(content)

        # await httpx.get(
        #     url="http://192.168.178.37/api/UoghabPi6o43qbmxud5U76fjgKF6BPtgznFCM-FT/lights/3/state/"
        # )

    else:

        await asyncio.sleep(2)

    print("request finished")


async def number_counter() -> None:
    for i in range(10):
        print(i)
        await asyncio.sleep(0.03)


async def main() -> None:
    task1 = asyncio.create_task(request_sim(True))
    task2 = asyncio.create_task(number_counter())

    await task1


if __name__ == "__main__":
    asyncio.run(main())
