from discord.ext import commands
import random

class Shufflers(commands.Cog):
  def __init__(self, main):
    self.bot = main

  @commands.command(name='shuffle', help='Shuffle word(s)')
  async def shuffler(self, ctx, *, word: str):
      wordl = list(word)
      random.shuffle(wordl)
      await ctx.send(''.join(wordl))
  
  @commands.command(name='shufflebyword', help='Shuffle every word')
  async def shuffleword(self, ctx, *, wordl: str):
      wordl = wordl.split(" ")
      newsentence = []
      for byword in range(len(wordl)):
        wordl1 = list(wordl[byword])
        wordl2 = random.sample(wordl1, len(wordl1))
        newsentence1 = ""
        for wjoin in wordl2:
          newsentence1 += wjoin
        newsentence.append(newsentence1 + ' ')
      wordl = newsentence
      await ctx.send(''.join(wordl))

  @commands.command(name='shufflesentence', help='Shuffle words to make a weird sentence.')
  async def makesentence(self, ctx, *, sentence: str):
      wordlist = sentence.split(' ')
      wordlist1 = list(wordlist)
      random.shuffle(wordlist1)
      await ctx.send(' '.join(wordlist1))

def setup(main):
  main.add_cog(Shufflers(main))