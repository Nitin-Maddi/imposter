# Imposter

A Discord bot that automates the word distribution for the "Imposter" party game. It uses AI to generate words and sends them directly to players via Discord DMs.

## How It Works

In the Imposter game:
- All players receive the same secret word, except for one player (the imposter) who receives a different but related word
- Players take turns giving clues about their word without revealing it
- The group tries to identify the imposter based on their clues

This bot automates the word distribution by:
1. Generating words using Google's Gemini AI based on a category you choose
2. Sending each player their word via Discord DM
3. Supporting multiple rounds while tracking previously used words

## Prerequisites

- Python 3.12+
- [UV](https://docs.astral.sh/uv/) package manager
- A Discord Bot Token
- A Google Gemini API Key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/imposter.git
cd imposter
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Reset Token" to get your bot token
4. Enable "Message Content Intent" under Privileged Gateway Intents
5. Go to "OAuth2" > "URL Generator", select "bot" scope, and generate an invite link
6. Use the link to invite the bot to your server

### 4. Get a Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key

### 5. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```
DISCORD_BOT_TOKEN=your_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Run the bot:

```bash
uv run python main.py
```

Follow the prompts:

1. Enter the number of players
2. Enter each player's Discord user ID (right-click user > Copy User ID)
3. Enter a category for the words (e.g., "fruits", "movies", "animals")
4. The bot will generate words and DM each player
5. After each round, choose whether to play again

## Getting Discord User IDs

To copy a user's Discord ID:
1. Enable Developer Mode in Discord (Settings > App Settings > Advanced > Developer Mode)
2. Right-click on a user and select "Copy User ID"

## License

MIT
