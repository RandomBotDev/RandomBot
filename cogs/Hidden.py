from discord.ext import commands
import discord
import random

class Hidden(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  @commands.command(hidden=True)
  async def support(self, ctx):
    embed = discord.Embed()
    embed.add_field(name="Need help?", value="Click [here](https://randombot.tk/support) to join the support server.")
    await ctx.send(embed=embed)
  
  @commands.command(hidden=True)
  async def invite(self, ctx):
    embed = discord.Embed()
    embed.add_field(name="Want to invite me?", value="Click [here](https://randombot.tk/invite) to invite me to a server.")
    await ctx.send(embed=embed)
  
  @commands.command(hidden=True)
  async def botinfo(self, ctx):
            hexlist = '01234567890abcdef'
            colorhex = ''
            for makecolor in range(0,6):
              genhex = random.choice(hexlist)
              colorhex = colorhex + genhex
            color = discord.Color(int(colorhex, 16))
            embed = discord.Embed(color=color)
            embed.add_field(name="Users", value=str(len(self.bot.users)), inline=False)
            embed.add_field(name="Servers", value=str(len(self.bot.guilds)), inline=False)
            if ctx.author.name == ctx.author.display_name:
              embed.set_footer(text=f'Requested by {ctx.author.display_name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            else:
              embed.set_footer(text=f'Requested by {ctx.author.display_name} ({ctx.author.name}#{ctx.author.discriminator})', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(main):
  main.add_cog(Hidden(main))