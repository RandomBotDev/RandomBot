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
          y="Yes "
          n="No "
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

  @commands.command(name="giveaway")
  async def gstart(self, ctx, channel:discord.TextChannel, gtime:int, *, reward):
    gtimes = 0
    embed = discord.Embed(title="New giveaway!")
    embed.add_field(name="Prize", value=reward)
    embed.add_field(name="Time", value=f'{gtime} seconds')
    gembed = await channel.send(embed=embed)
    await gembed.add_reaction("🎉")
    nembed = None
    while gtime > 0:
      await sleep(1)
      gtime = gtime - 1
      nembed = discord.Embed(title="New giveaway!")
      nembed.add_field(name="Prize", value=reward)
      nembed.add_field(name="Time", value=f'{gtime} seconds')
      await gembed.edit(embed=nembed)
    chosenuser = random.choice(greactors)
    while True:
      if chosenuser == "RandomBot#5275":
        if gtimes == 100:
          wembed = discord.Embed(title=f'Nobody won the {reward} giveaway.')
          await gembed.edit(embed=wembed)
          return 
        else:
          gtimes = gtimes + 1
      else:
        wembed = discord.Embed(title=f'{chosenuser} won the {reward} giveaway!')
        await gembed.edit(embed=wembed)
        return 

  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    if str(reaction.emoji) == "🎉":
      uinfo = f'{user}'
      greactors.append(uinfo)

  @commands.command(name='decide', help="Decide on something")
  async def chooser(self, ctx, *, thing):
    options = ['Yes', 'For sure', 'Maybe', 'I don\'t know', 'No', 'Definently not', 'Definently']
    choic3 = random.choice(options)
    await ctx.send(choic3)
  
  @commands.command(name="randomuser")
  async def ruser(self, ctx):
    cuser = random.choice(ctx.guild.members)
    user = f'{cuser.display_name} ({cuser})'
    return await ctx.send(user)

def setup(main):
  main.add_cog(Choosers(main))