import discord
import responses  
from discord import Intents
intents = Intents.default()



import os
from dotenv import load_dotenv
load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)  # corrected response to responses
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:  # corrected the indentation here
        print(e)

def run_discord_bot():  
    TOKEN = os.getenv('TOKEN')
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
         async def on_message(message):
        if message.author == client.user:
            return


        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: `{user_message}` ({channel})")

        if user_message[0]=='?':

            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    

    client.run(TOKEN)



