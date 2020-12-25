from discord.ext import commands
import random

class Shufflers(commands.Cog):
  def __init__(self, main):
    self.bot = main

  @commands.command(name='shuffle', help='Shuffle word(s)')
  async def shuffler(self, ctx, *, word: str):
      wordl = list(word)
      random.shuffle(wordl)
      if ''.join(wordl) == "nigger":
          await ctx.send("no")
      elif ''.join(wordl) == "condom":
          await ctx.send("no")
      elif ''.join(wordl) == "condoms":
          await ctx.send("no")
      elif ''.join(wordl) == "niger":
          await ctx.send("no")
      elif ''.join(wordl) == "cum":
          await ctx.send("no")
      elif ''.join(wordl) == "sex":
          await ctx.send("no")
      elif ''.join(wordl) == "sexy":
          await ctx.send("no")
      elif ''.join(wordl) == "anal":
          await ctx.send("no")
      elif ''.join(wordl) == "anus":
          await ctx.send("no")
      elif ''.join(wordl) == "cock":
          await ctx.send("no")
      elif ''.join(wordl) == "balls":
          await ctx.send("no")
      elif ''.join(wordl) == "fuck":
          await ctx.send("no")
      elif ''.join(wordl) == "shit":
          await ctx.send("no")
      elif ''.join(wordl) == "crap":
          await ctx.send("no")
      elif ''.join(wordl) == "ass":
          await ctx.send("no")
      elif ''.join(wordl) == "asshole":
          await ctx.send("no")
      elif ''.join(wordl) == "dick":
          await ctx.send("no")
      elif ''.join(wordl) == "bitch":
          await ctx.send("no")
      elif ''.join(wordl) == "butt":
          await ctx.send("no")
      elif ''.join(wordl) == "penis":
          await ctx.send("no")
      elif ''.join(wordl) == "butts":
          await ctx.send("no")
      else:
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
      if ''.join(wordl) == "nigger":
          await ctx.send("no")
      elif ''.join(wordl) == "condom":
          await ctx.send("no")
      elif ''.join(wordl) == "condoms":
          await ctx.send("no")
      elif ''.join(wordl) == "niger":
          await ctx.send("no")
      elif ''.join(wordl) == "cum":
          await ctx.send("no")
      elif ''.join(wordl) == "sex":
          await ctx.send("no")
      elif ''.join(wordl) == "sexy":
          await ctx.send("no")
      elif ''.join(wordl) == "anal":
          await ctx.send("no")
      elif ''.join(wordl) == "anus":
          await ctx.send("no")
      elif ''.join(wordl) == "cock":
          await ctx.send("no")
      elif ''.join(wordl) == "balls":
          await ctx.send("no")
      elif ''.join(wordl) == "fuck":
          await ctx.send("no")
      elif ''.join(wordl) == "shit":
          await ctx.send("no")
      elif ''.join(wordl) == "crap":
          await ctx.send("no")
      elif ''.join(wordl) == "ass":
          await ctx.send("no")
      elif ''.join(wordl) == "asshole":
          await ctx.send("no")
      elif ''.join(wordl) == "dick":
          await ctx.send("no")
      elif ''.join(wordl) == "bitch":
          await ctx.send("no")
      elif ''.join(wordl) == "butt":
          await ctx.send("no")
      elif ''.join(wordl) == "penis":
          await ctx.send("no")
      elif ''.join(wordl) == "butts":
          await ctx.send("no")
      else:
          await ctx.send(''.join(wordl))

  @commands.command(name='shufflesentence', help='Shuffle words to make a weird sentence.')
  async def makesentence(self, ctx, *, sentence: str):
      wordlist = sentence.split(' ')
      wordlist1 = list(wordlist)
      random.shuffle(wordlist1)
      if ' '.join(wordlist1) == "nigger":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "condom":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "condoms":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "niger":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "cum":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "sex":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "sexy":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "anal":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "anus":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "cock":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "balls":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "fuck":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "shit":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "crap":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "ass":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "asshole":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "dick":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "bitch":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "butt":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "penis":
          await ctx.send("no")
      elif ' '.join(wordlist1) == "butts":
          await ctx.send("no")
      else:
          await ctx.send(' '.join(wordlist1))

def setup(main):
  main.add_cog(Shufflers(main))