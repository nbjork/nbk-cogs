from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random

url = 'http://whiskeycrow.com/Graal/heads/'
ext = 'png'

def list_dir(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

class Ghead:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ghead(self, head):

        files = list_dir(url, ext)
        if head + ".png" in files:
            await self.bot.say("http://whiskeycrow.com/Graal/heads/" + head + ".png")
        else:
            await self.bot.say(head + " not found, noob")

    @commands.command()
    async def randhead(self):

        files = list_dir(url, ext)
        await self.bot.say("http://whiskeycrow.com/Graal/heads/" + random.choice(files))

def setup(bot):
    bot.add_cog(Ghead(bot))
