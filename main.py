import os
import os
import os
import os
import discord
from discord.ext import commands
import random
from discord import Permissions
import colorama
from colorama import Fore
import os
from discord.utils import get

TOKEN = os.environ["TOKEN"]

os.system('cls & mode 85,20 & title [GYPSY CRUSADER NUKE BOT] ')
os.system('cls')
bot = commands.Bot(command_prefix="$", case_insensitive=False, self_bot=False)
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

...
from discord.ext import commands
...

# Change only the no_category default string
help_command = commands.DefaultHelpCommand(
    no_category = 'Anti Nuking Commands'
)

# Create the bot and pass it the modified help_command
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('$'),
    help_command = help_command
)

with open('badwords.txt') as file:
    file = file.read().split()

RACIST_MESSAGE=("kys fucking retarded monkey")

@bot.event
async def on_ready():
    Channel = bot.get_channel(1127397829095202926)
    Text= "react here to verify monkey"
    Moji = await Channel.send(Text)
    await Moji.add_reaction('✔️')
@bot.event
async def on_reaction_add(reaction, user):
    Channel = bot.get_channel(1127397829095202926)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "✔️":
      Role = discord.utils.get(user.server.roles, name="verified")
      await user.add_roles(Role)

async def status_task():
 while True:
    await bot.change_presence(activity=discord.Game(name="VR:The Train Ran on Trusts Mother Experience"))
    await asyncio.sleep(200000)
  
@bot.event
async def on_ready():
    print(f"Bot Is Ready Nigger")
    bot.loop.create_task(status_task())

import convert 

@bot.command()
async def bww(ctx):
 with open("bww.txt") as f:
    content = "\n".join(f.readlines())

 await ctx.send(content)

import zipfile
@bot.command()
async def zip(ctx):
    channel_id = 1127397829095202926
    zip_file = "I-1.zip"

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        file_names = zip_ref.namelist()
        content = []

        for file_name in file_names:
            with zip_ref.open(file_name) as file:
                content.append(file.read().decode())

    channel = bot.get_channel(channel_id)
    await channel.send("\n".join(content))

@bot.command()
async def site(ctx):
    channel_id = 1127397829095202926
    with open("sites.txt") as f:
        content = "\n".join(f.readlines())
    channel = bot.get_channel(channel_id)
    await channel.send(content)

@bot.command()
async def train(ctx):
    channel_id = 1127397829095202926
    with open("train.txt") as f:
        content = "\n".join(f.readlines())
    channel = bot.get_channel(channel_id)
    await channel.send(content)
    await asyncio.sleep(10)#minutes

send_message ="The Train Party Experience Is leaving!"
	
@bot.command()
async def train2(ctx):
    channel_id = 1127397829095202926
    with open("train2.txt") as f:
        content = "\n".join(f.readlines())
    channel = bot.get_channel(channel_id)
    await channel.send(content)
    await asyncio.sleep(60)#seconds
@bot.command()
async def nsfw(ctx):
    channel_id = 1151367339254759514 # Replace with the actual channel ID
    with open("porn.txt") as f:
        content = "\n".join(f.readlines())
    channel = bot.get_channel(channel_id)
    await channel.send(content)


@bot.command()
async def crunchyroll(ctx):

    await bot.wait_until_ready()
    channel = bot.get_channel(1127397829095202926)
    while True:
        await channel.send('Working!', file=discord.File("crunchyroll.txt"))
        await asyncio.sleep(10000000000)#hours


@bot.command()
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()
@commands.has_role('.')
async def giveaway(ctx, timing, winners: int, *, prize):
  await ctx.send('Okay, making a giveaway!', delete_after=3)
  gwembed = discord.Embed(
    title=":tada: Giveaway :tada:",
    description=f'Prize: {prize}',
    color=0xb4e0fc
  )
  time = convert(timing)
  gwembed.set_footer(text=f"This giveaway ends {time} seconds from this message.")
  gwembed = await ctx.send(embed=gwembed)
  await gwembed.add_reaction(":tada:")
  await asyncio.sleep(time)
  message = await ctx.fetch_message(gwembed.id)
  users = await message.reactions[0].users().flatten()
  users.pop(users.index(ctx.guild.me))
  if len(users) == 0:
    await ctx.send("No winner was decided.")
    return
  for i in range(winners):
    winner = random.choice(users)
    await ctx.send(f"Congrats to: {winner}!")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def prison(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Prisoner")
    await member.edit(roles=[])
    await member.add_roles(sped)
    await ctx.send(f"{member} is imprisoned!")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def strip(ctx:commands.Context, member: discord.Member):
    everyone = ctx.guild.default_role
    try:
        await member.edit(roles=[everyone])
        await ctx.send(f"Yoink gimme dem roles bitch.")
    except discord.Forbidden:
        await ctx.send("Are you retarded or something? i can only strip niggas under my role.")
    except discord.HTTPException:
        await ctx.send("Failed to remove roles.")

stripped_role="familia"
@bot.command()
@commands.has_permissions(manage_roles=True)
async def restore(ctx, user: discord.Member):
    guild = ctx.guild
    stripped_role = None
    
    # Find the stripped role in the guild
    for role in guild.roles:
        if role.name == "familia""-18""Members""NSFW Verified""Female""Black""rizz":
            stripped_role = role
            break
    
    if not stripped_role:
        await ctx.send("Stripped role does not exist in this server.")
        return
    
    try:
        # Remove the stripped role from the user
        await user.remove_roles("rizz")
        await ctx.send(f"Successfully restored roles for user {user.display_name}.")
    except discord.Forbidden:
        await ctx.send("I do not have the necessary permissions to restore roles.")
    except discord.HTTPException:
        await ctx.send("Failed to restore roles due to an error.")


        

@bot.command(pass_context = True)
@commands.is_owner()
async def r(ctx, *args):
    channel = bot.get_channel(1108806378832789574)
    await channel.send(RACIST_MESSAGE)



@bot.command(pass_context=True)
async def gr(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

                
			

@bot.command(name="massunban")
@commands.has_any_role("MAGNUM XL")
async def massunban(self, context, *user_ids: int):
    for u in user_ids:
        user_object = await self.client.fetch_user(u)
        await context.guild.unban(user_object)

@bot.command()
async def supportt(ctx, *, reason = None):
    guild = ctx.guild
    user = ctx.author
    await ctx.message.delete() # Deletes the message of the author
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    channel = await guild.create_text_channel(f'Ticket {user}', overwrites=overwrites)
    await channel.send(f"{user.mention}")
    supem = discord.Embed(title=f"{user} Created a ti.", description= "", color=0x00ff00)
    supem.add_field(name="reason", value=f"``{reason}``")
    supem.set_footer(text=f"staff will be with you shortly")
    await channel.send(embed=supem)

intents = discord.Intents.default()
intents.members = True
import datetime

@bot.command(aliases=['usrinfo', 'user', 'whois'])
async def userinfo(ctx, *, member:discord.Member = None):
    if not member:
            member = ctx.message.author

    embed=discord.Embed(
      title="User Information", 
      timestamp=datetime.utcnow(),
      colour=discord.Colour.random()
      )
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_fieeld(name="Name", value=member.name)
    embed.add_field(name="Nickname", value=member.nick)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join Position", value=str(members.index(member)+1))
    embed.add_field(name="Status", value=member.status)
    await ctx.send(embed=embed)



@bot.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str('Munches Rise Up')

  owner = str('A Nigger')
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)




      


@bot.command(description='Bans a specified member but racistly')
@commands.has_permissions(ban_members=True)
async def rb(self, ctx, member: discord.Member, *, reason="unspecified reason"):
    if member.id == ctx.author.id:
        await ctx.send("You cannot ban yourself, sorry! :)")
        return

    if member.id == ctx.bot.owner_id:
        await ctx.send("Sorry, the bot owner cannot be banned.")
        return

    if member.top_role >= ctx.author.top_role:
        await ctx.send("You can only moderate members below your role")
        return

    await member.ban(reason=reason)
    reasonEmbed = discord.Embed(
        description=f'Successfully banned the nigger monkey{member.mention} for {reason}\n \n ',
        colour=0xFF0000
    )
    reasonEmbed.set_author(name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
    reasonEmbed.set_footer(text=f"Banned by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar_url))
    await ctx.send(embed=reasonEmbed)



@bot.command(aliases=['c', 'purge', 'p'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=3):
    await ctx.channel.purge(limit = amount)
        
    await ctx.message.delete()

@bot.command(aliases=['dm'])
async def DM(ctx, user : discord.User, *, msg):
    try:
        await user.send(msg)
        await ctx.send(f':white_check_mark: Your Message has been sent')
    except:
        await ctx.send(':x: had their dm close, message not sent')
        await ctx.message.delete()

@bot.command()
@commands.has_permissions(kick_members = True)
async def rk(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await member.send("u are a nigger lover and have been kicked from **3XIV**")
    await member.kick(reason=reason)
    await ctx.message.delete()
  

@bot.command(description='racist ban #2')
@commands.has_permissions(ban_members = True)
async def rb2(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " is a dirty nigger lover and has been from banned the server ")
    await member.ban(reason=reason)
    await ctx.message.delete()




@bot.command()
async def role(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def idle(ctx):
    await bot.change_presence(status=discord.Status.idle)
    print(Fore.GREEN + "Set The Bots Status To Idle" + Fore.RESET)
    await ctx.message.delete()
import asyncio

@bot.command()
async def afk(ctx, mins):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} has gone afk for {mins} minutes.")
    await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def offline(ctx):
    await bot.change_presence(status=discord.Status.offline)
    print(Fore.Blue + "Set The Bots Status To Offline" + Fore.RESET)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def streaming(ctx):
   await bot.change_presence(status=discord.Status.Streaming)
   print(Fore.Blue + "Set The Bots Status To Streaming" + Fore.RESET)

@bot.command()
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def dr(ctx, role_name, *, exceptions=None):
    deleted_roles = 0
    if exceptions == None:
        guild = bot.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == role_name:
                await role.delete()
                deleted_roles += 1
        if deleted_roles == 0:
            await ctx.send("Couldn't find any roles with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} roles')
    else:
        try:
            exceptions_cont = exceptions.split(' --exc ')
            
            if len(exceptions_cont) > 1:
                role_name = role_name + ' ' + exceptions_cont[0]
                if not exceptions_cont[1] == '':
                    exceptions = exceptions_cont[1].split(', ')
            else:
                exceptions = exceptions.split(', ')
            
        except Exception as e:
            exceptions = exceptions.split(', ')
           
        guild = bot.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == '@everyone':
                continue
            if role.name == role_name:

                for exception in exceptions:
                    if int(role.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await role.delete()
                    deleted_roles += 1

        if deleted_roles == 0:
            await ctx.send("Couldn't find any roles with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} roles')
case_insensitive=False


@bot.command()
@commands.has_permissions(manage_channels=True, administrator=True)
async def delete(ctx, channel_name, *, exceptions='None'):
    deleted_channels = 0
    if exceptions == 'None':
        guild = bot.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:
                await channel.delete()
                deleted_channels += 1
        if deleted_channels == 0:
            await ctx.send("O can't find any fuckin channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass
    else:

        exceptions_cont = exceptions.split(', ')
        guild = bot.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:

                for exception in exceptions_cont:
                    if int(channel.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await channel.delete()
                    deleted_channels += 1

        if deleted_channels == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass
        await ctx.message.delete()

@bot.command()
async def dmall(ctx,desc):
    title = f'message from {ctx.message.author}'
    await ctx.send('Sending messages!')
    for member in ctx.guild.members:
        embed = discord.Embed(title=title, description=desc)
        await member.send(embed=embed)
        print('Sent a message!')
        await asyncio.sleep(3)




@bot.command()
async def passs(ctx, blunt):
    members = ctx.guild.members  # Get all members in the server
    random_member = random.choice(members)
    await ctx.send(f"The {blunt} has been passed to {random_member.mention}!")



bot.run(TOKEN, bot=True)
































