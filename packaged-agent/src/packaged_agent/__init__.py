from .agent import *


async def main():
    response = await Runner.run(agent, "Hi!")
    print(response.final_output)


def run():
    import asyncio
    asyncio.run(main())
