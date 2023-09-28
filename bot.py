import discord
import os
from discord.ext import commands
from commands import (
    walle,
    walle100,
    walle200,
    wallehelp,
    walleclearhistory,
    wallewordcount,
)


# Create a Discord bot
intents = discord.Intents.default()
intents.message_content = True  # Enable the intent to read message content

bot = commands.Bot(command_prefix="/", intents=intents)

# Add commands to bot
bot.add_command(walle)
bot.add_command(walle100)
bot.add_command(walle200)
bot.add_command(wallehelp)
bot.add_command(walleclearhistory)
bot.add_command(wallewordcount)

# Run the bot with your Discord token
bot.run(os.getenv("DISCORD_API_KEY"))
