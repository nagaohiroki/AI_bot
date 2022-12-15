import discord
import os
import openai


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    openai.api_key = os.environ['OPENAI_API_KEY']
    print('AI bot login')


@client.event
async def on_message(message):
    if message.author.bot:
        print('bot echo')
        return
    if client.user not in message.mentions:
        print('no mention')
        return
    response = createAI(message.clean_content)
    print(response)
    text = response['choices'][0]['text']
    await message.channel.send(text)


def createAI(content):
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=content,
        max_tokens=1024,
        temperature=0.5)


client.run(os.environ['AI_BOT_TOKEN'])
