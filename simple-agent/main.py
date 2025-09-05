from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled
load_dotenv()
set_tracing_disabled(True)

agent = Agent(
    name="Hello Agent",
    instructions="Respond with a creative and quirky greeting.",
    model="litellm/gemini/gemini-2.5-flash"
)


async def main():
    response = await Runner.run(agent, "Hi!")
    print(response.final_output)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
