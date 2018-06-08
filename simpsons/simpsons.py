from discord.ext import commands
import compuglobal

class Simpsons:

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def sgif(self):
    simpsons = compuglobal.Frinkiac()
    screencap = simpsons.get_random_screencap()
    gif = await screencap.get_gif_url()
    self.bot.say(gif)
