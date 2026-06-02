import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté!')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="bienvenue")
    
    if channel:
        embed = discord.Embed(
            title="👁️ Bienvenue dans L'Œil !",
            description=f"Salut {member.mention}, bienvenue !",
            color=discord.Color.blue()
        )
        embed.add_field(name="📖 Commence ici", value="#comment-ça-marche", inline=False)
        embed.add_field(name="💳 S'abonner", value="https://whop.com/l-oeil", inline=False)
        embed.set_footer(text="Bon courage ! 🚀")
        
        await channel.send(embed=embed)

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
