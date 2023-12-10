from disnake import Intents
from disnake.ext.commands import Bot
from misc import Env
import os


def start_bot():
    intents = Intents.all()
    intents.message_content = True
    intents.members = True
    try:
        bot = Bot(command_prefix='/', intents=intents)
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                bot.load_extension(f"cogs.{file[:-3]}")
                print(f'cogs.{file[:-3]} loaded')
    except Exception as e:
        print(e)
    print('Started')

    bot.run(Env.TOKEN)


start_bot()

