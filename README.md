# AI_bot

ChatGPT discord bot

## Discrod Setting(enable Intents)

https://discordpy.readthedocs.io/ja/latest/discord.html

MyApplications -> SETTINGS/Bot -> Privileged Gateway Intents
[PRESENCE INTENT] 
[SERVER MEMBERS INTENT]
[MESSAGE CONTENT INTENT]


## Server Setting

```
SETX /M AI_BOT_TOKEN "aaaa"
SETX /M OPENAI_API_KEY "bbbb"
python pip install -U openai
python pip install -U "discord.py[voice]"
```

## Launch

```
python ai_bot.py
```

## Message

change discord setting role name to AI -> AI_bot(avoid wrong mention)

```
@AI good morning
@AI /img good morning
```

or on TEXT CHANNELS "ai"

```
good morning
/img good morning
```

![gm.png](gm.png) 
