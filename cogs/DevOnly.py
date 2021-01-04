from discord.ext import commands
import sys
import os
import discord
import contextlib
import io
import asyncio
import time
import random

class DevOnly(commands.Cog):
  def __init__(self, main):
    self.bot = main

  async def _shutdown(self):
        os.system('clear')
        await self.bot.logout()
        await self.bot.close()
  
  @commands.command(hidden=True)
  async def shutdown(self, ctx):
        if ctx.author.id != 716250356803174511:
            return

        await ctx.send('Shutting down...')
        await self._shutdown()
  
  @commands.command(hidden=True)
  async def halp(self, ctx, user):
        if ctx.author.id != 716250356803174511:
            return
        await ctx.send("help")
        while True:
          uspam = await ctx.send(user)
          await uspam.delete()

  @commands.command(hidden=True)
  async def restart(self, ctx):
        if ctx.author.id != 716250356803174511:
            return

        await ctx.send('Restarting...')
        await self._shutdown()
        script = sys.argv[0]
        if script.startswith(os.getcwd()):
            script = script[len(os.getcwd()):].lstrip(os.sep)

        if script.endswith('__main__.py'):
            args = [sys.executable, '-m', script[:-len('__main__.py')].rstrip(os.sep).replace(os.sep, '.')]
        else:
            args = [sys.executable, script]
        os.execv(sys.executable, args + sys.argv[1:])

  @commands.command(hidden=True)
  async def resetstatus(self, ctx):
    if ctx.author.id != 716250356803174511:
      return
    activity = discord.Game(name="rb.help | Invite the bot: https://bit.ly/InviteRandomBot")
    await self.bot.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send("Successfully reset the status.")

  @commands.command(hidden=True)
  async def status(self, ctx, presence : discord.Status, atype, *, botstatus):
    if ctx.author.id != 716250356803174511:
      return
    if atype == "playing" or atype == "Playing":
      status = discord.Game(name=botstatus)
      await self.bot.change_presence(status=presence, activity=status)
    elif atype == "listening" or atype == "Listening":
      activity = discord.Activity(type=discord.ActivityType.listening, name=botstatus)
      await self.bot.change_presence(activity=activity)
    elif atype == "watching" or atype == "Watching":
      activity = discord.Activity(type=discord.ActivityType.watching, name=botstatus)
      await self.bot.change_presence(activity=activity)
    elif atype == "streaming" or atype == "streaming":
      activity = discord.Streaming(name=botstatus, url="https://twitch.tv/discord")
      await self.bot.change_presence(activity=activity)
    await ctx.send(f"Successfully changed the presence to {presence} with the type {atype} and status {botstatus}.")
  
  @commands.command(hidden=True)
  async def starttyping(self, ctx):
    if ctx.author.id != 716250356803174511:
      return
    await ctx.send("Typing...")
    while True:
      async with ctx.typing():
        pass

  @commands.command(hidden=True)
  async def stoptyping(self, ctx):
    if ctx.author.id != 716250356803174511:
      return
    await ctx.send('Stopped typing.')
    await self._shutdown()
    script = sys.argv[0]
    if script.startswith(os.getcwd()):
        script = script[len(os.getcwd()):].lstrip(os.sep)

    if script.endswith('__main__.py'):
        args = [sys.executable, '-m', script[:-len('__main__.py')].rstrip(os.sep).replace(os.sep, '.')]
    else:
        args = [sys.executable, script]
    os.execv(sys.executable, args + sys.argv[1:])

  @commands.command(hidden=True)
  async def ping(self, ctx, times : int):
    if ctx.author.id != 716250356803174511:
      #return
      if times > 99:
        return  
    pingmgr = ""
    if times == 1:
      pingmgr = await ctx.send(f'Pinging {times} time')
    else:
      pingmgr = await ctx.send(f'Pinging {times} times')
    pings = []
    await asyncio.sleep(1)
    for pingr in range(1, times+1):
      t1 = time.time()
      await pingmgr.edit(content=f"Ping {pingr}")
      t2 = time.time()
      ptime = t2 - t1
      pings.append(ptime)
      await asyncio.sleep(1)
    aping = sum(pings)
    aping = aping / times * 1000
    await pingmgr.edit(content=f'{aping} ms')
  
  @commands.command(hidden=True)
  async def syseval(self, ctx, *, command : str):
    if ctx.author.id != 716250356803174511:
      return
    str_obj = io.StringIO()
    try:
        with contextlib.redirect_stdout(str_obj):
            os.system(command)
    except Exception as e:
        return await ctx.send(f"An error occured: {e}")
    await ctx.send(f'''{str_obj.getvalue()}''')
  
  @commands.command(hidden=True)
  async def eval(self, ctx, *, command : str):
    if ctx.author.id != 716250356803174511:
      return
    str_obj = io.StringIO()
    try:
        with contextlib.redirect_stdout(str_obj):
            exec("print(" + command + ")")
    except Exception as e:
      hexlist = '01234567890abcdef'
      colorhex = ''
      for makecolor in range(0,6):
        genhex = random.choice(hexlist)
        colorhex = colorhex + genhex
      color = discord.Color(int(colorhex, 16))
      embed = discord.Embed(title="Evaluation Failed...", color=color)
      embed.add_field(name="Input", value=ctx.message.content.lower()[8:])
      embed.add_field(name="Output", value=f'''{e}''')
      return await ctx.send(embed=embed)
    hexlist = '01234567890abcdef'
    colorhex = ''
    for makecolor in range(0,6):
      genhex = random.choice(hexlist)
      colorhex = colorhex + genhex
    color = discord.Color(int(colorhex, 16))
    embed = discord.Embed(title="Evaluation Success!", color=color)
    embed.add_field(name="Input", value=ctx.message.content.lower()[8:])
    embed.add_field(name="Output", value=f'''{str_obj.getvalue()}''')
    await ctx.send(embed=embed)
  
  @commands.command(hidden=True)
  async def boteval(self, ctx, *, command : str):
    if ctx.author.id != 716250356803174511:
      return
    str_obj = io.StringIO()
    try:
        with contextlib.redirect_stdout(str_obj):
            exec("print(self.bot." + command + ")")
    except Exception as e:
        return await ctx.send(f"An error occured: {e}")
    await ctx.send(f'''{str_obj.getvalue()}''')
  
  
  @commands.command(hidden=True)
  async def ctxeval(self, ctx, *, command : str):
    if ctx.author.id != 716250356803174511:
      return
    str_obj = io.StringIO()
    try:
        with contextlib.redirect_stdout(str_obj):
            exec("print(ctx." + command + ")")
    except Exception as e:
        return await ctx.send(f"An error occured: {e}")
    await ctx.send(f'''{str_obj.getvalue()}''')
  
  @commands.command(hidden=True)
  async def nickname(self, ctx, member : discord.Member, *, nick=None):
      if ctx.author.id != 716250356803174511:
        return
      embed = discord.Embed(title = "Nickname Successfully Changed!", color=random.randint(0, 16777215))
      embed.add_field(name = "Original Name:", value = f"{member.display_name}")
      if nick == None:
        await member.edit(name=self.bot.user.name)
      await member.edit(nick=nick)
      embed.add_field(name = "New Nickname:", value = f"{member.display_name}")
      await ctx.send(embed=embed)

def setup(main):
  main.add_cog(DevOnly(main))