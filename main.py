import discord
from discord.ext import commands 

bot= commands.Bot('!')

@bot.event
async def on_ready():
  print('>>bot is online<<')


bot.run('OTE4NTAxMDAyOTU5ODAyMzc5.YbIKuA.B-T2MDVNQVs1ZD8zanlLswddwAc')
