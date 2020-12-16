from discord.ext import commands
import discord

class Events(commands.Cog):
  def __init__(self, main):
    self.bot = main
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    await ctx.send(f'An error occured: {str(error)}')
  
  @commands.Cog.listener()
  async def on_ready(self):
    activity = discord.Game(name="rb.help | Invite the bot: https://bit.ly/InviteRandomBot")
    await self.bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'{self.bot.user.name}#{self.bot.user.discriminator} is ready to go!')
  
  @commands.Cog.listener() 
  async def on_message(self, message):
    for x in message.mentions:
        if(x==self.bot.user):
          if message.content.split() == ['<@!716309071854174268>']:
            embed = discord.Embed(color=0xffffff, title="Hello, my name is RandomBot!")
            embed.add_field(name="The developer", value="GD Tom#3216", inline=False)
            embed.add_field(name="Somthing went wrong?", value="Join the support server. https://discord.gg/PFkSPFc7cM", inline=False)
            embed.add_field(name="Invite me to your server!", value="https://randombot.daguacaplushy.repl.co/invite", inline=False)
            embed.add_field(name="My prefix:", value="rb.", inline=False)
            await message.channel.send(embed=embed)

def setup(main):
  main.add_cog(Events(main))