from discord.ext import commands
import openai
from dotenv import load_dotenv
import os

# Load your OpenAI API key from environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to send a user message to GPT-3 and get a response
def generate_response(prompt):
    message_history = [
        {
            "role": "system",
            "content": "You are a helpful assistant that provides information.",
        }
    ]
    user_message = {"role": "user", "content": prompt}
    message_history.append(user_message)

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
        max_tokens=200,  # Adjust max_tokens as needed
    )

    # Extract chatGPT response
    chatgpt_response = response["choices"][0]["message"]
    return chatgpt_response["content"]


# Define bot commands
@commands.command()
async def walle(ctx, *, prompt: str):
    response = generate_response(prompt)
    await ctx.send(response)


@commands.command()
async def walle100(ctx, *, prompt: str):
    prompt += ", Provide a concise response in 100 words or less:\n"
    response = generate_response(prompt)
    await ctx.send(response)


@commands.command()
async def walle200(ctx, *, prompt: str):
    prompt += ", Summarize the following in 200 words or less:\n"
    response = generate_response(prompt)
    await ctx.send(response)


@commands.command()
async def wallehelp(ctx):
    help_message = "WALLE Bot Commands:\n\n"
    help_message += "/walle [prompt]: Get a response based on your prompt.\n"
    help_message += (
        "/walle100 [prompt]: Get a concise response in 100 characters or less.\n"
    )
    help_message += "/walle200 [prompt]: Summarize the input in 200 words or less.\n"
    help_message += "/walleclearhistory: clear the bots current message history\n"
    help_message += "/wallewordcount: get the previous messages word count. If no previous message is found, return error message\n"

    await ctx.send(help_message)


@commands.command()
async def walleclearhistory(ctx):
    # Clear the message history by removing all messages in the channel
    async for message in ctx.channel.history():
        if message.author == ctx.bot.user:
            await message.delete()

    await ctx.send("Message history cleared.")


@commands.command()
async def wallewordcount(ctx):
    # Get the previous message in the channel
    async for message in ctx.channel.history(limit=2):
        if message != ctx.message:  # Exclude the current command message
            previous_message = message.content
            break
    else:
        await ctx.send("No previous message found.")
        return

    # Calculate the word count
    word_count = len(previous_message.split())

    # Send the word count as a response
    await ctx.send(f"The previous message has {word_count} words.")
