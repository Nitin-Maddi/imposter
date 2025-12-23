import os
import discord


async def send_dm(client: discord.Client, user_id: int, message: str) -> bool:
    """Send a DM to a Discord user. Returns True on success, False on failure."""
    try:
        user = await client.fetch_user(user_id)
        await user.send(message)
        return True
    except discord.NotFound:
        print(f"User {user_id} not found.")
        return False
    except discord.Forbidden:
        print(f"Cannot DM user {user_id} (DMs may be disabled).")
        return False
    except Exception as e:
        print(f"Error sending DM to {user_id}: {e}")
        return False


def get_bot_token() -> str:
    """Get the Discord bot token from environment variables."""
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        raise ValueError("DISCORD_BOT_TOKEN environment variable is not set")
    return token
