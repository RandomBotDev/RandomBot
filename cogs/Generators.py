from discord.ext import commands
import random
import discord
import urllib

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
  async def pgen(self, ctx, length:int=20):
      chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*();,./':<>?\[]}{-=+"
      password=""
      if length > 5:
          for passlength in range(0,length):
              genchar=random.choice(chars)
              password=password+genchar
          if ctx.guild == None:
            await ctx.send(password)
          else:
            await ctx.author.send(password)
            await ctx.send('Check your DM\'s.')
      else:
          await ctx.send("There must be at least 6 characters.")
  
  @commands.command(name='binarygen')
  async def bgen(self, ctx, length : int):
    bin = '01'
    gbin = ''
    for bgener1 in range(0, length):
      for bgener2 in range(0,8):
        cbin = random.choice(bin)
        gbin = gbin + cbin
      gbin = gbin + ' '
    await ctx.send(gbin)
  
  @commands.command(name='eject')
  async def ejectuser(self, ctx, *, user : discord.Member="you"):
    if user == "you":
      user = ctx.author
    crew = ["black", "blue", "brown", "cyan", "darkgreen", "lime", "orange", "pink", "purple", "red", "white", "yellow"]
    crewcolor = random.choice(crew)
    imp = ["true", "false"]
    isimpostor = random.choice(imp)
    username = str(user.name)
    urlname = urllib.parse.quote(username)
    ejected = f'https://vacefron.nl/api/ejected?name={urlname}&impostor={isimpostor}&crewmate={crewcolor}'
    embed = discord.Embed()
    embed.set_image(url=ejected)
    await ctx.send(embed=embed)

def setup(main):
  main.add_cog(Generators(main))