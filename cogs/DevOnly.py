from discord.ext import commands
import sys
import os
import discord

class DevOnly(commands.Cog):
  def __init__(self, main):
    self.bot = main

  async def _shutdown(self):
        os.system('clear')
        await self.bot.logout()
        await self.bot.close()
        self.bot.loop.stop()
  @commands.command(hidden=True)
  async def shutdown(self, ctx):
        if ctx.author.id != 716250356803174511:
            return

        await ctx.send('Shutting down...')
        await self._shutdown()

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
  async def status(self, ctx, presence : discord.Status, *, botstatus):
    if ctx.author.id != 716250356803174511:
      return
    status = discord.Game(name=botstatus)
    await self.bot.change_presence(status=presence, activity=status)
    await ctx.send(f"Successfully changed the presence to {presence} with the status {status}.")
  
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
  async def ping(self, ctx):
    if ctx.author.id != 716250356803174511:
      return
    await ctx.send(f'{self.bot.latency*1000 : .3f} ms')

def setup(main):
  main.add_cog(DevOnly(main))