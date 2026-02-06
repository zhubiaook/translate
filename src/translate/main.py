import asyncio
import sys
import uuid
import warnings

from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from translate.agent import get_agent

warnings.filterwarnings("ignore")


async def query_agent(
    runner: Runner,
    user_id: str,
    session_id: str,
    question: str,
) -> None:
    """Query the agent with a single question and print the response."""
    content: types.Content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=question)],
    )

    # Enable SSE streaming mode, return response token by token
    run_config: RunConfig = RunConfig(streaming_mode=StreamingMode.SSE)

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content,
        run_config=run_config,
    ):
        if event.content and event.partial and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print()  # Final newline


async def interactive_mode(
    runner: Runner,
    user_id: str,
    session_id: str,
) -> None:
    """Run the agent in an interactive loop."""
    print("Type 'quit' or 'exit' to exit.\n")

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! 👋")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye! 👋")
            break

        print("")
        await query_agent(runner, user_id, session_id, user_input)
        print("-" * 50 + "\n")


async def run() -> None:
    """Main entry point for the translate CLI."""
    session_service: InMemorySessionService = InMemorySessionService()

    runner: Runner = Runner(
        agent=get_agent(),
        app_name="translate",
        session_service=session_service,
    )

    user_id: str = "cli_user"
    session_id: str = str(uuid.uuid4())

    # Create the session
    try:
        _ = await session_service.create_session(
            app_name="translate",
            user_id=user_id,
            session_id=session_id,
        )
    except Exception as e:
        print(f"Failed to create session: {e}", file=sys.stderr)
        sys.exit(1)

    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        # Join all arguments as the question
        question: str = " ".join(sys.argv[1:])
        await query_agent(runner, user_id, session_id, question)
    else:
        # No arguments - enter interactive mode
        await interactive_mode(runner, user_id, session_id)


def main() -> None:
    asyncio.run(run())
