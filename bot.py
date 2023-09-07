import discord
import responses  

import os
from dotenv import load_dotenv
load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)  # corrected response to responses
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:  # corrected the indentation here
        print(e)

def run_discord_bot():  # added the def keyword
    global TOKEN
    TOKEN = os.getenv('TOKEN')
    client = discord.Client()
    print("Script is running!")
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')  # changed 'not running' to 'now running'

    client.run(TOKEN)



