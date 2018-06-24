import discord
from discord.ext import commands

#commands have prefix: & or when its mentioned
bot = commands.Bot(command_prefix=commands.when_mentioned_or('&'))

token = "TOKEN HERE"

#pass_context is needed if you want to use ctx (context)
@bot.command(pass_context=True)
#repeat being the command name
#* meaning text doesnt split with a space
# text: str meaning that the expected value is a string.
async def repeat(ctx, *, text: str):
    #you can use bot.say in commands
    #bot says whatever you put after the command, and who it is from
    await bot.say(text + ", from " + ctx.message.author.display_name)

#more advanced commond, but made easy by discord.ext
@bot.command()
#a discord member object (mention) being the expected value
async def member_info(member: discord.Member):
    #chack to see if the member is playing anything
    if member.game != '':
    #bot say the game the member is playing
        await bot.say(member.game)
    #and say the name colour
    await bot.say(member.colour)

#without notes, names changed so a error wont occur when running the bot:

@bot.command(pass_context=True)
async def echo(ctx, *, text: str):
    await bot.say(text + ", from " + ctx.message.author.display_name)

@bot.command()
async def game_colour(member: discord.Member):
    if member.game != None:
        await bot.say(member.game)
    await bot.say(member.colour)

bot.run(token)
