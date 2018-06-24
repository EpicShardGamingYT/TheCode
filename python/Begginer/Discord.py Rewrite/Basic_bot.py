import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="any_prefix_as_much_as_you_want_")
client = discord.Client()


@bot.event
async def on_ready():
  print('My son has been awaken from dead')
  
@bot.command()
async def cookie(ctx):
"""Cookie from your son"""
  await ctx.send(":cookie:")
  await ctx.message.add_reaction("\U0001f36a")
  
@bot.command()
async def ping(ctx):
"""Ping pong"""
  await ctx.send("ctx.message.author.mention, Pong")
  
 @bot.command()
async def userinfo(ctx, member : discord.Member):
    embed = discord.Embed(title="User Info for {}".format(member.name), colour=mc)
    embed.add_field(name="Username:", value=member.name, inline=True)
    embed.add_field(name="User ID:", value=member.id, inline=True)
    embed.add_field(name="Is Bot:", value=member.bot)
    embed.add_field(name="Created at:", value=member.created_at, inline=True)
    embed.add_field(name="Nickname:", value=member.display_name)
    embed.add_field(name="Status:", value=member.status, inline=True)
    embed.add_field(name="Playing:", value=member.game)
    embed.add_field(name="Highest Role:", value=member.top_role, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

bot.run(' ')#Insert token inside the quotes!
