from discord.ext import commands
import discord

class Shards(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  @commands.Cog.listener()
  async def on_shard_connect(self,shard_id):
    if shard_id == 0:
      activity = discord.Game(name=f"Starting shard {shard_id+1}.")
      await self.bot.change_presence(status=discord.Status.online, activity=activity)
      print(f"{self.bot.user} has connected.")
    else:
      activity = discord.Game(name=f"Starting shard {shard_id+1}.")
      await self.bot.change_presence(status=discord.Status.online, activity=activity)
      print(f"Shard {shard_id} has connected.")
      print(f"Shard {shard_id+1} is connecting.")

  @commands.Cog.listener()
  async def on_shard_disconnect(self,shard_id):
    print(f"Shard {shard_id} has disconnected.")

  @commands.Cog.listener()
  async def on_shard_resume(self,shard_id):
    print(f"Shard {shard_id} has reconnected.")

  @commands.Cog.listener()
  async def on_shard_ready(self,shard_id):
    print(f"Shard {shard_id} is ready to go!")

def setup(main):
  main.add_cog(Shards(main))