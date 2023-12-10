from disnake.ext import commands
import disnake
from misc import Config
from ui import AuthModal


class AuthButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='👷 Опубликовать', style=disnake.ButtonStyle.gray, custom_id='authbutton')
    async def authbutton(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_modal(modal=AuthModal())
