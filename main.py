from disnake import Intents
from disnake.ext.commands import Bot
from dotenv import load_dotenv

import os


def start_bot():
    intents = Intents.all()
    intents.message_content = True
    intents.members = True
    load_dotenv(".env")

    try:
        bot = Bot(command_prefix='/', intents=intents)
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                bot.load_extension(f"cogs.{file[:-3]}")
                print(f'cogs.{file[:-3]} loaded')
    except Exception as e:
        print(e)
    print('Started')

    bot.run(os.environ.get('BOT_TOKEN', 'define me!'))


start_bot()

