# WALLE Discord Bot

This is a Discord bot named WALLE that uses OpenAI's GPT-3 model to generate responses to user prompts.
# WALLE bot

## Features

- Responds to user prompts with AI-generated text using OpenAI's GPT3.5 Turbo.
- Provides concise responses in 100 words or less.
- Summarizes input in 200 words or less.
- Clears the bot's message history.
- Counts the words in the previous message.

![image](https://github.com/Minsukim2827/Discord-OpenAI-Chatbot/assets/122320786/711dcf94-e808-4dca-9b79-c2e65fca8e11)


## Commands

- `/walle [prompt]`: Get a response based on your prompt.
- `/walle100 [prompt]`: Get a concise response in 100 words or less.
- `/walle200 [prompt]`: Summarize the input in 200 words or less.
- `/walleclearhistory`: Clear the bot's current message history.
- `/wallewordcount`: Get the previous message's word count. If no previous message is found, it returns an error message.

## Setup

1. Clone this repository.
2. Install the required Python packages: `discord.py`, `openai`, and `python-dotenv`.
3. Set up your OpenAI API key and Discord API key in your environment variables.
4. Run `bot.py` to start the bot.

## Usage

Invite the bot to your Discord server and use the commands listed above.

## Note

This bot uses OpenAI's GPT-3 model, which may incur costs depending on usage.
