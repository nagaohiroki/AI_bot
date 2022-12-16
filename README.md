# AI_bot

ChatGPT discord bot

## Discrod Setting(enable Intents)

https://discordpy.readthedocs.io/ja/latest/discord.html

MyApplications -> SETTINGS/Bot -> Privileged Gateway Intents
[PRESENCE INTENT] 
[SERVER MEMBERS INTENT]
[MESSAGE CONTENT INTENT]


## Server Setting

windows

```
SETX /M AI_BOT_TOKEN "aaaa"
SETX /M OPENAI_API_KEY "bbbb"
python -m pip install -r requirements.txt
python ai_bot.py
```

mac, linux

```
$ export AI_BOT_TOKEN=aaaa
$ export OPENAI_API_KEY=bbbb
$ sudo python3 -m pip install -r requirements.txt
$ nohup python3 mineserver-op.py > ./out.log & # 
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
