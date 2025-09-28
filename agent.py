from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import google, noise_cancellation
import sounddevice as sd
import os

# Load environment variables
load_dotenv(".env")

from prompt import AGENT_INSTRUCTIONS, AGENT_RESPONSE


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=AGENT_INSTRUCTIONS)


async def entrypoint(ctx: agents.JobContext):
    # Create a session with Google Gemini Realtime
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            api_key=os.getenv("GOOGLE_API_KEY"),
            voice="Puck",
            temperature=0.8,
            instructions=AGENT_INSTRUCTIONS,
        ),
    )

    # Start the session
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Generate reply from prompt
    await session.generate_reply(
        instructions=AGENT_RESPONSE,
    )

    # Optional greeting (can be customized)
    # await session.generate_reply(instructions="Hello! How can I help you today?")


if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
