from google import genai
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()
client = genai.Client()

# Gemini prompting
# prompt = "Who won the 2025 World Series?"
# prompt += "And also provide the final score of game 7 of the 2025 World Series."

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=prompt
# )

# if response != None:
#     print(response.text)
# else:
#     print("broke")


# Discord bot work
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    author = message.author
    if message.author == bot.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


bot.run(token)