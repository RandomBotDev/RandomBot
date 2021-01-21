from discord.ext import commands
import random
import discord
from asyncio import sleep

class Choosers(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  @commands.command(name='yesorno', help='Randomly choose yes or no.')
  async def fiftyfifty(self, ctx, yespercent: int=50, nopercent: int=50):
      if nopercent + yespercent == 100:
          y="Yes. "
          n="No. "
          ychance=y*yespercent
          nchance=n*nopercent
          yn=ychance+nchance
          yn2 = yn.split(" ")
          result=random.choice(yn2)
          await ctx.send(result)
      else:
          await ctx.send("Invalid percentage or value.")

  @commands.command(name='flipcoin', help='Flip a coin.')
  async def flip(self, ctx):
      h="Heads! "
      t="Tails! "
      hchance=h*50
      tchance=t*50
      ht=hchance+tchance
      ht2 = ht.split(" ")
      result=random.choice(ht2)
      await ctx.send(result)
  
  global greactors
  greactors = []

  @commands.command(name="giveaway", description="Start a giveaway.")
  async def gstart(self, ctx, channel:discord.TextChannel, gtime:int, *, reward):
    if gtime > 86400:
      return await ctx.send("I can only do giveaways shorter than 1 day.")
    global greactors
    gtimes = 0
    embed = discord.Embed(title="New giveaway!")
    embed.add_field(name="Prize", value=reward)
    embed.add_field(name="Time", value=f'{gtime} seconds')
    embed.add_field(name="Host", value=f'{ctx.author.name}#{ctx.author.discriminator}')
    gembed = await channel.send(embed=embed)
    await gembed.add_reaction("🎉")
    nembed = None
    while gtime > 0:
      await sleep(1)
      gtime = gtime - 1
      nembed = discord.Embed(title="New giveaway!")
      nembed.add_field(name="Prize", value=reward)
      nembed.add_field(name="Time", value=f'{gtime} seconds')
      nembed.add_field(name="Host", value=f'{ctx.author.name}#{ctx.author.discriminator}')
      await gembed.edit(embed=nembed)
    chosenuser = random.choice(greactors)
    while True:
      if chosenuser == "RandomBot#5275" or chosenuser == f"{ctx.author.name}#{ctx.author.discriminator}":
        if gtimes == 100:
          wembed = discord.Embed(title=f'Nobody won the {reward} giveaway.')
          await gembed.edit(embed=wembed)
          greactors = []
          return 
        else:
          gtimes = gtimes + 1
          chosenuser = random.choice(greactors)
      else:
        wembed = discord.Embed(title=f'{chosenuser} won the {reward} giveaway!')
        await gembed.edit(embed=wembed)
        greactors = []
        return

  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    if str(reaction.emoji) == "🎉":
      uinfo = f'{user}'
      greactors.append(uinfo)
  
  @commands.Cog.listener()
  async def on_reaction_remove(self, reaction, user):
    if str(reaction.emoji) == "🎉":
      uinfo = f'{user}'
      greactors.remove(uinfo)

  @commands.command(name="choose", help="Seperate choices with \" + \"")
  async def c(self,ctx, *, options):
    osplit = options.split(" + ")
    ping = False
    for option in osplit:
      if option.startswith("<@") or option.startswith("@here") or option.startswith("@everyone"):
        ping = True
    if ping:
      return await ctx.send("I can't ping.")
    choice = random.choice(osplit)
    await ctx.send(f"I choose ***{choice}***.")

  @commands.command(name='decide', help="Decide on something for you")
  async def chooser(self, ctx, *, thing):
    options = ['Yes.', 'For sure!', 'Maybe.', 'I don\'t know.', 'No.', 'Definently not.', 'Definently!']
    choic3 = random.choice(options)
    await ctx.send(choic3)

def setup(main):
  main.add_cog(Choosers(main))