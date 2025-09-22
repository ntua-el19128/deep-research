import asyncio
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

load_dotenv()

console = Console()

async def main() -> None:
    console.print("Hey there")
    console.print("Deep Research Tool")

    query = Prompt.ask("What would you like to learn")

    if not query.strip():
        console.print("")
        return 
    

if __name__ == "__main__":
    asyncio.run(main())


