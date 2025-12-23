import asyncio
import discord
from dotenv import load_dotenv
from llm_client import generate_words
from discord_client import send_dm, get_bot_token


def validate_user_id(user_id: str) -> bool:
    """Basic validation for Discord user IDs (17-19 digit numbers)."""
    return user_id.isdigit() and 17 <= len(user_id) <= 19


def collect_user_ids() -> list[int]:
    """Interactively collect Discord user IDs from the user."""
    while True:
        try:
            count = int(input("How many Discord users? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    user_ids = []
    for i in range(1, count + 1):
        while True:
            user_id = input(f"Enter Discord user ID {i}: ").strip()
            if validate_user_id(user_id):
                user_ids.append(int(user_id))
                break
            else:
                print("Invalid format. Discord user IDs are 17-19 digit numbers.")

    return user_ids


async def send_messages(user_ids: list[int], words: list[str]):
    """Connect to Discord and send DMs to all users."""
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}\n")

        success_count = 0
        for idx, user_id in enumerate(user_ids):
            print(f"Sending DM to {user_id}...", end=" ")
            if await send_dm(client, user_id, words[idx]):
                print("Success!")
                success_count += 1
            else:
                print("Failed!")

        print(f"\nDone! Sent {success_count}/{len(user_ids)} messages.")
        await client.close()

    token = get_bot_token()
    await client.start(token)


def main():
    load_dotenv()

    user_ids = collect_user_ids()
    category = input("Enter a category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    used_words: set[str] = set()
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")
        print(f"Generating words for category: {category}...")

        try:
            words = generate_words(category, len(user_ids), used_words)
        except Exception as e:
            print(f"Error generating words: {e}")
            return

        print(f"Generated: {words}\n")

        # Add words to used set
        used_words.update(words)

        print("Connecting to Discord...")
        asyncio.run(send_messages(user_ids, words))

        # Ask for another round
        another = input("\nPlay another round? (y/n): ").strip().lower()
        if another != 'y':
            print("Thanks for playing!")
            break

        round_num += 1


if __name__ == "__main__":
    main()
