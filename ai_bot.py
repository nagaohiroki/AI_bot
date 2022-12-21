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
    if message.channel.name != 'ai':
       if client.user not in message.mentions:
            print(f'no mention. at: {message.channel}')
            return
    text = ''
    try:
        tag = '/img'
        if tag in message.clean_content:
            text = create_ai_image(message.clean_content.replace(tag, ''))
        else:
            text = create_ai_chat(message)
    except Exception as e:
        text = str(e)
    await message.channel.send(text)


chat_context = {}
def create_ai_chat(message):
    global chat_context
    context_text = chat_context.get(message.guild.id)
    if not context_text:
        context_text = ''
    prompt = f'{context_text}{message.author.name}:{message.clean_content}\nAI:'
    # clamp max_token
    max_token = 4097
    prompt = prompt[-max_token:]
    ai_text = create_ai_text(prompt)
    chat_context[message.guild.id] = f'{prompt}{ai_text}\n'
    return ai_text


def create_ai_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.9)
    print(response)
    return response.choices[0]['text']


def create_ai_image(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    print(response)
    return response.data[0]['url']


client.run(os.environ['AI_BOT_TOKEN'])
