import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = '&')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Thank you for joining Alastria!'))
    print('bot is online!')

@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.send(f" You have been kicked from Alastria ")
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kick", description=f" {member.mention}- Kicked from Alastria",colour=discord.Colour.orange())
    await ctx.send(embed=embed)
    await ctx.send(f'https://tenor.com/view/anime-clannad-kick-go-away-clannad-after-story-gif-14835708')
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.send(f" You have been banned from Alastria ")
    embed = discord.Embed(title="Ban", description=f" {member.mention}- Banned from Alastria",colour=discord.Colour.orange())
    await ctx.send(embed=embed)
    await ctx.send(f'https://tenor.com/view/anime-mad-ban-punch-gif-17117340')
@client.command()
@has_permissions(ban_members=True)
async def clearc(ctx, ammout = 100000):
    await ctx.channel.purge(limit=ammout)
@client.command()
@has_permissions(ban_members=True)
async def clear(ctx, lammout = 30):
    await ctx.channel.purge(limit=lammout)
@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="unban", description=f" {member.mention}- unbanned from Alastria",colour=discord.Colour.orange())
            await ctx.send(embed=embed)
            return
@client.command(description="Unmutes a specified user.")
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="꒰ ៸៸ Muted🍢 ⊹ ₊˚꒱")

   await member.remove_roles(mutedRole)
   await member.send(f" You have unmuted from Alastria: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.orange())
   await ctx.send(embed=embed)
@client.command(description="Mutes a specified user.")
@has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="꒰ ៸៸ Muted🍢 ⊹ ₊˚꒱")

   await member.add_roles(mutedRole)
   await member.send(f" You have muted from Alastria: - {ctx.guild.name}")
   embed = discord.Embed(title="mute", description=f" muted-{member.mention}",colour=discord.Colour.orange())
   await ctx.send(embed=embed)
@client.command(description="Shows a help desk")
@commands.has_permissions(ban_members=True)
async def Ahelp(ctx):
    embed = discord.Embed(title="HELP DESK", description=f"""
     &ban- to ban anyone
     &unban - to unban anyone
     &mute - to mute anyone
     &unmute - to unmute anyone
     &kick - to kick anyone from
     &Ahelp - to access Help Desk
     """,colour=discord.Colour.orange())
    await ctx.send(embed=embed)
client.run('OTMxNTUxOTgwNDAzNDQxNjk0.YeGFYw.4VStlAkKqT0al9AxPiN_lPzwqw0')
