import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = response.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        except Exeption as e:
            print(e)

            def run_discord_bot:
                TOKEN = "MTE0ODk5ODQ0MTEwMDM5MDUzMQ.GJ_aQh.aL-u9CWQXrxXl2QDKuAI9QjRft1jMF0ttRrzLk"
                client = discord.Client()

                @client.event
                async def on_ready():
                    print(f'{client.user} is not running')

                    client.run(TOKEN)