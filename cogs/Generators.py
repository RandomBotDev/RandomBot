from discord.ext import commands
import random
import discord

class Generators(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  @commands.command(name='colorgen', aliases=['colourgen', 'color', 'colour'], help='Generate a random hex color')
  async def gencolor(self, ctx):
    hexlist = '01234567890abcdef'
    colorhex = ''
    for makecolor in range(0,6):
      genhex = random.choice(hexlist)
      colorhex = colorhex + genhex
    color = discord.Color(int(colorhex, 16))
    colrgb = discord.Color.to_rgb(color)
    embed=discord.Embed(title=f'{color} {colrgb}', color=color)
    await ctx.send(embed=embed)

  @commands.command(name='impostor', help='Are you an impostor?')
  async def areyouimpostor(self, ctx):
      roles = ['Crewmate', 'Crewmate', 'Impostor', 'Crewmate', 'Crewmate']
      role = random.choice(roles)
      await ctx.send(role)

  @commands.command(name='passwordgen', help='Generate a random password.')
  async def gen(self, ctx, length:int=20):
      chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*();,./':<>?\[]}{-=+"
      password=""
      if length > 5:
          for passlength in range(0,length):
              genchar=random.choice(chars)
              password=password+genchar
          await ctx.author.send(password)
      else:
          await ctx.send("There must be at least 6 characters.")

def setup(main):
  main.add_cog(Generators(main))