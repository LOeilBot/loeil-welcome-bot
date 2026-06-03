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
    print(f"✅ Nouveau membre détecté: {member.name}")
    channel = discord.utils.get(member.guild.channels, name="bienvenue")
    print(f"Channel trouvé: {channel}")
    
    if channel:
        try:
            embed = discord.Embed(
                title="👁️ Bienvenue dans L'Œil !",
                description=f"Salut {member.mention}, bienvenue !",
                color=discord.Color.blue()
            )
            embed.add_field(name="📖 Commence ici", value="#comment-ça-marche", inline=False)
            embed.add_field(name="💳 S'abonner", value="https://whop.com/l-oeil", inline=False)
            embed.set_footer(text="Bon courage ! 🚀")
            
            await channel.send(embed=embed)
            print(f"✅ Message envoyé à {member.name}")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    else:
        print("❌ Channel bienvenue non trouvé!")

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
