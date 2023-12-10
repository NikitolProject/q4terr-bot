from disnake.ext import commands
import disnake
from misc import Config
from ui import AuthButton


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name='authorization', description='настройка авторизации',
                            guild_ids=Config.ALL_GUILDS)
    async def auth(self, ctx):
        pass

    @commands.has_permissions(administrator=True)
    @auth.sub_command(name='start', description='Отправить сообщение авторизации',
                      guild_ids=Config.ALL_GUILDS)
    async def auth_message(self, ctx):
        view = AuthButton()
        emb = disnake.Embed(title='Публикация объявления',
                            description='Чтобы создать пост о поиске работы или сотрудника нажмите на кнопку опубликовать\n\n'
                                        '👷  Перед публикацией объявления обязательно ознакомься с правилами.',
                            color=0x2b2d31)
        await ctx.send('Выполнено!', ephemeral=True)
        await ctx.channel.send(embed=emb, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return
        self.bot.add_view(AuthButton(), message_id=Config.MESSAGE_ID)


def setup(bot):
    bot.add_cog(Auth(bot))
