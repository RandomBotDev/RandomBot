from discord.ext import commands
import random

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

  @commands.command(name='decide', help="Decide on something")
  async def chooser(self, ctx, *, thing):
    options = ['Yes', 'For sure', 'Maybe', 'I don\'t know', 'No', 'Definently not', 'Definently']
    choic3 = random.choice(options)
    await ctx.send(choic3)

def setup(main):
  main.add_cog(Choosers(main))