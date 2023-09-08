import discord
import responses  
from discord import Intents
intents = Intents.default()
intents.message_content = True



import os
from dotenv import load_dotenv
load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message) 
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:  
        print(e)

def run_discord_bot():  
    TOKEN = os.getenv('TOKEN')
    print(TOKEN)
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print("Bot is ready!")
        
    @client.event
    async def on_message(message):
        print(message.content)

        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: `{user_message}` ({channel})")

        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)




