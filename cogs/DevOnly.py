from discord.ext import commands
import sys
import os
import discord
import contextlib
import io
import asyncio
import time
import random
import ast
import psutil
from googletrans import Translator


class DevOnly(commands.Cog):
  def __init__(self, main):
    self.bot = main

  async def _shutdown(self):
        os.system('clear')
        await self.bot.logout()
        await self.bot.close()
  
  def insert_returns(self, body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        self.insert_returns(body[-1].body)
        self.insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        self.insert_returns(body[-1].body)
  
  @commands.command(hidden=True)
  async def eval2(self, ctx, *, cmd):
    if ctx.author.id != 716250356803174511:
  	  return await ctx.send('An error occured: Command "eval2" is not found')
    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    if "ban" in cmd.lower() or "kick" in cmd.lower() or "messages:" in cmd.lower() or "add_role" in cmd.lower() or "create_" in cmd.lower():
      await ctx.send("I can't do that.")
      return

    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    self.insert_returns(body)

    env = {
        'bot': self.bot,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__,
        'asyncio': asyncio
    }
    exec(compile(parsed, filename="<ast>", mode="exec"), env)

    result = (await eval(f"{fn_name}()", env))
    if type(result) == discord.Message:
      pass
    else:
      try:
        await ctx.send(result)
      except Exception as e:
        if str(e) == "Command raised an exception: HTTPException: 400 Bad Request (error code: 50006): Cannot send an empty message" or str(e) == "400 Bad Request (error code: 50006): Cannot send an empty message":
          return
        else:
          await ctx.send(f"An error occured: {e}")

  @commands.command(name="memusage", hidden=True)
  async def getmem(self, ctx):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "memusage" is not found')
    await ctx.send(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) + " MB")
  
  @commands.command(hidden=True)
  async def shutdown(self, ctx):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "shutdown" is not found')

    await ctx.send('Shutting down...')
    await self._shutdown()

  @commands.command(hidden=True)
  async def translate(self, ctx, *, message : str):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "translate" is not found')
    translator = Translator()
    translated = translator.translate(message)
    await ctx.send(f"Output: {translated.text}")
  
  @commands.command(hidden=True)
  async def restart(self, ctx):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "restart" is not found')

    await ctx.send('Restarting...')
    await self._shutdown()
    script = sys.argv[0]
    if script.startswith(os.getcwd()):
      script = script[len(os.getcwd()):].lstrip(os.sep)

      if script.endswith('main.py'):
        args = [sys.executable, '-m', script[:-len('main.py')].rstrip(os.sep).replace(os.sep, '.')]
      else:
        args = [sys.executable, script]
      os.execv(sys.executable, args + sys.argv[1:])

  @commands.command(hidden=True)
  async def resetstatus(self, ctx):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "resetstatus" is not found')
    activity = discord.Game(name="rb.help | Invite the bot: https://bit.ly/InviteRandomBot")
    await self.bot.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send("Successfully reset the status.")

  @commands.command(hidden=True)
  async def status(self, ctx, presence : discord.Status, atype, *, botstatus):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "status" is not found')
    if botstatus == "None":
      botstatus = None
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
      activity = discord.Streaming(name=botstatus, url="https://twitch.tv/guacaplushy")
      await self.bot.change_presence(activity=activity)
    await ctx.send(f"Successfully changed the presence to {presence} with the type {atype} and status {botstatus}.")
  
  @commands.command(hidden=True)
  async def starttyping(self, ctx):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "starttyping" is not found')
    await ctx.send("Typing...")
    while True:
      async with ctx.typing():
        pass
  
  @commands.command(hidden=True)
  async def delm(self, ctx, limit : int):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "delm" is not found')
    messages = await ctx.channel.history(limit=limit).flatten()
    mlen = 0
    for message in messages:
      if message.author == self.bot.user:
        await message.delete()
        mlen = mlen + 1
    await ctx.author.send(f"Deleted {mlen} of my messages.")

  @commands.command(hidden=True)
  async def stoptyping(self, ctx):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "stoptyping" is not found')
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
      #return await ctx.send('An error occured: Command "ping" is not found')
      if times > 99:
        return await ctx.send('An error occured: Command "ping" is not found')
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
  async def eval(self, ctx, *, command : str):
    if ctx.author.id != 716250356803174511:
      return await ctx.send('An error occured: Command "eval" is not found')
    if "ban" in command.lower() or "kick" in command.lower() or "messages:" in command.lower() or "add_role" in command.lower() or "create_" in command.lower():
      await ctx.send("I can't do that.")
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
      embed.add_field(name="Input", value=command)
      embed.add_field(name="Output", value=f'''{e}''')
      return await ctx.send(embed=embed)
    hexlist = '01234567890abcdef'
    colorhex = ''
    for makecolor in range(0,6):
      genhex = random.choice(hexlist)
      colorhex = colorhex + genhex
    color = discord.Color(int(colorhex, 16))
    embed = discord.Embed(title="Evaluation Success!", color=color)
    embed.add_field(name="Input", value=command)
    embed.add_field(name="Output", value=f'''{str_obj.getvalue()}''')
    await ctx.send(embed=embed)
  
  @commands.command(hidden=True)
  async def nickname(self, ctx, member : discord.Member, *, nick=None):
      if ctx.author.id != 716250356803174511:
        return await ctx.send('An error occured: Command "nickname" is not found')
      embed = discord.Embed(title = "Nickname Successfully Changed!", color=random.randint(0, 16777215))
      embed.add_field(name = "Original Name:", value = f"{member.display_name}")
      if nick == None:
        await member.edit(name=self.bot.user.name)
      await member.edit(nick=nick)
      embed.add_field(name = "New Nickname:", value = f"{member.display_name}")
      await ctx.send(embed=embed)

def setup(main):
  main.add_cog(DevOnly(main))