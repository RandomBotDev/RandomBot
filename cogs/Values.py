from discord.ext import commands
import random

class Values(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  @commands.command(name='randomnumber', help='Generates a random number.')
  async def randomnumberexec(self, ctx, nmbr: int=1000000):
    response = random.randint(0,nmbr)
    await ctx.send(response)

  @commands.command(name='luckynumber', help='Generate a luckynumber.')
  async def gennumber(self, ctx):
      newnumber = random.randint(0,100)
      await ctx.send(newnumber)

  @commands.command(name='cooltest', help='How cool are you?')
  async def test(self, ctx):
    await ctx.send(f'{ctx.author.mention}, You are {random.randint(0,100)} percent cool.')
  
  @commands.command(name='risktest', help='How risky is something?')
  async def tester(self, ctx, *, idea):
    risk = random.randint(0,100)
    await ctx.send(f'{idea} is {risk}% risky')
  
  @commands.command(name='smarttest', help='How smart are you?')
  async def stester(self, ctx):
    smart = random.randint(0,100)
    await ctx.send(f'{ctx.author.mention}, You are {smart}% smart')

  @commands.command(name='rate', help='How good is something?')
  async def rs(self, ctx, *, thing):
    v1 = random.randint(0,5)
    v2 = random.randint(0,9)
    if v1 == 5 and v2 > 0:
      await ctx.send(f'I rate {thing} 5 out of 5 stars')
      return
    if v1 == 5 and v2 == 0:
      await ctx.send(f'I rate {thing} 5 out of 5 stars')
      return
    if v1 == 0 and v2 == 0:
      await ctx.send(f'I rate {thing} 0 out of 5 stars')
      return
    else:
      await ctx.send(f'I rate {thing} {v1}.{v2} out of 5 stars')
  
  @commands.command(name='dice', help='Rolls dice for you.')
  async def roll(self, ctx, numberofdice: int, numberofsides: int):
      vdice = [
          str(random.choice(range(1, numberofsides + 1)))
          for _ in range(numberofdice)
      ]
      await ctx.send(', '.join(vdice))

def setup(main):
  main.add_cog(Values(main))