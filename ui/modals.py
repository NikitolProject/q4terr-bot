from disnake.ext import commands
import disnake
import re
from disnake import TextInputStyle
from misc import Config


class AuthModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label='Название',
                placeholder='Невероятный строитель!',
                custom_id='name',
                style=TextInputStyle.short,
                max_length=32,
            ),
            disnake.ui.TextInput(
                label='Описание',
                placeholder='Очень жёстко строю, туда-сюда!',
                custom_id='descr',
                style=TextInputStyle.long,
            ),
            disnake.ui.TextInput(
                label='Теги(выберите один)',
                placeholder='Перестройщик/ресурсер/дизайнер/скинодел/другое',
                custom_id='tags',
                style=TextInputStyle.short,
                max_length=12
            ),
            disnake.ui.TextInput(
                label='Сроки',
                placeholder='',
                custom_id='datetime',
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label='Ссылка на портфолио',
                placeholder='https:/imgur.com/someurl',
                custom_id='portfolio',
                style=TextInputStyle.short,
            ),
        ]
        super().__init__(title="Публикация объявления", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        tags = inter.text_values['tags']
        tag_list = ['перестройщик', 'перестроищик', 'ресурсер', 'дизайнер', 'дизаинер', 'скинодел', 'другое']
        if tags.lower() in tag_list:
            name = inter.text_values['name']
            descr = inter.text_values['descr']
            datetime = inter.text_values['datetime']
            portfolio = inter.text_values['portfolio']
            emb = disnake.Embed(title=name, description=f'**Описание**\n{descr}', color=0xffa200)
            emb.add_field(name='Тэги', value=tags, inline=False)
            emb.add_field(name='Сроки', value=datetime, inline=False)
            emb.add_field(name='Портфолио', value=portfolio, inline=False)
            emb.add_field(name='Контактные данные', value=f'@{inter.author.mention}')
            match tags.lower():
                case 'перестройщик':
                    channel = inter.guild.get_channel(Config.REBUILD)
                    await channel.send(embed=emb)
                case 'ресурсер':
                    channel = inter.guild.get_channel(Config.RESOURCE)
                    await channel.send(embed=emb)
                case 'дизайнер':
                    channel = inter.guild.get_channel(Config.DESIGN)
                    await channel.send(embed=emb)
                case 'скинодел':
                    channel = inter.guild.get_channel(Config.SKINS)
                    await channel.send(embed=emb)
                case 'другое':
                    channel = inter.guild.get_channel(Config.OTHER)
                    await channel.send(embed=emb)
            await inter.response.send_message('Вы успешно опубликовали сообщение!', ephemeral=True)
        else:
            await inter.response.send_message('Неправильно указаны теги, попробуйте ещё раз!', ephemeral=True)
