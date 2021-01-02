from discord.ext import commands
import discord
import random

class Events(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, ZeroDivisionError):
      pass
    else:
      await ctx.send(f'An error occured: {str(error)}')
  
  @commands.Cog.listener()
  async def on_ready(self):
    activity = discord.Game(name="rb.help | Invite the bot: https://randombot.tk/invite")
    await self.bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'{self.bot.user.name}#{self.bot.user.discriminator} is ready to go!')

  @commands.Cog.listener() 
  async def on_message(self, message):
    for x in message.mentions:
        if(x==self.bot.user):
          if message.content.split() == ['<@!716309071854174268>'] or message.content.split() == ['<@716309071854174268>']:
            hexlist = '01234567890abcdef'
            colorhex = ''
            for makecolor in range(0,6):
              genhex = random.choice(hexlist)
              colorhex = colorhex + genhex
            color = discord.Color(int(colorhex, 16))
            embed = discord.Embed(color=color, title="Hello, my name is RandomBot!")
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/716309071854174268/a7de2db6f154711b022d8045fe2a238c.webp?size=512')
            embed.add_field(name="The developer", value="GD Tom#0001", inline=False)
            embed.add_field(name="Did something go wrong?", value="[Click this to join the support server.](https://randombot.tk/support)", inline=False)
            embed.add_field(name="Want to invite me to your server?", value="[Click this to invite me!](https://randombot.tk/invite)", inline=False)
            embed.add_field(name="About Me:", value="I started as a useless app, but then the developer\ndecided to make a bot. I was already in the developer\nportal so the developer took me and made me\na working bot. He already knew Python\nso he coded me. I am what he made.", inline=False)
            embed.add_field(name="My prefix:", value="rb.", inline=False)
            if message.author.name == message.author.display_name:
              embed.set_footer(text=f'Requested by {message.author.display_name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
            else:
              embed.set_footer(text=f'Requested by {message.author.display_name} ({message.author.name}#{message.author.discriminator})', icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

    with open('badwords.txt') as file:
      file = file.read().split()

    if message.author.id == self.bot.user.id:
      for badword in file:
        if badword in message.content.lower():
          await message.delete()
          await message.channel.send("no")

def setup(main):
  main.add_cog(Events(main))