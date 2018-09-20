from discord.ext import commands
import wikiquote
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Qotd:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def qotd(self):
        qotd = wikiquote.quote_of_the_day()
        await self.bot.say(qotd[0])
        await self.bot.say("- " + qotd[1])
        
    async def qsearch(self, sterm):
        search = wikiquote.quotes(sterm,max_quotes=3)
        await self.bot.say(search)

def setup(bot):
    bot.add_cog(Qotd(bot))
