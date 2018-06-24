import discord
import datetime

from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('&'))

token = 'TOKEN HERE'

#command version:
@bot.command()
async def embed():
    embed = discord.Embed(title = 'Test Embed', description = 'hello world')
    #0x meaning a hex color, FFFFFF being the hex code
    embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too like: discord.Embed(colour=0xFFFFFF)

    # Images
    embed.set_image(url = 'Image Url')
    embed.set_thumbnail(url = 'Image Url')

    embed.set_author(name = 'Author name', url = 'URL to open when name is clicked', icon_url = 'Image Url') #Appears above title, image is circle.
    embed.set_footer(text = 'Example footer', icon_url = 'Image Url') #footer is a small text att bottom, icon_url is a small image before the text
    embed.timestamp = datetime.datetime.utcnow() #a time stamp, example: sent yesterday at 2PM

    embed.add_field(name = 'Name [256 char max]', value = 'Content [1024 char]', inline=True)
    # max 25 fields

    #send the embed:
    await bot.say(embed=embed)

#on_message version (bad)
@bot.event
async def on_message(message):
    #message changed to prevent command used when on_message is wanted.
    if message.content.upper().startswith('!EMBED'):
        embed = discord.Embed(title = 'Test Embed', description = 'hello world')
        #0x meaning a hex color, FFFFFF being the hex code
        embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too like: discord.Embed(colour=0xFFFFFF)

        # Images
        embed.set_image(url = 'Image Url')
        embed.set_thumbnail(url = 'Image Url')

        embed.set_author(name = 'Author name', url = 'URL to open when name is clicked', icon_url = 'Image Url') #Appears above title, image is circle.
        embed.set_footer(text = 'Example footer', icon_url = 'Image Url') #footer is a small text att bottom, icon_url is a small image before the text
        #throws error, dont know a fix and someone else will have to fix it.
        embed.timestamp = datetime.datetime.utcnow() #a time stamp, example: sent yesterday at 2PM

        embed.add_field(name = 'Name [256 char max]', value = 'Content [1024 char]', inline=True)
        # max 25 fields

        #send the embed:
        await bot.send_message(message.channel, embed=embed)

bot.run(token)
