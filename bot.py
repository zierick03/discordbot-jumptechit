#pip install discord.py (uitvoeren in powershell)
import discord
import random
from discord.ext import commands

# Bot setup met intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=["/", "!"], intents=intents)

# Event: Bot is online
@bot.event
async def on_ready():
    print(f'✅ Bot is online als: {bot.user}')
    await bot.tree.sync()  # Zorg ervoor dat de slash-commando's worden gesynchroniseerd
    print("Slash-commando's zijn gesynchroniseerd!")

# Normale (prefix) commando's
@bot.command()
async def hoi(ctx):
    await ctx.send(f'Hoi {ctx.author.mention}! 👋')

@bot.command()
async def hallo(ctx):
    await ctx.send(f'Hallo {ctx.author.mention}, hoe gaat het? 😄')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.command()
async def randomgetal(ctx, start: int, einde: int):
    import random
    getal = random.randint(start, einde)
    await ctx.send(f'Het willekeurige getal tussen {start} en {einde} is: {getal}')

# Slash-commando's (werkt met / in Discord)
@bot.tree.command(name="hoi", description="Zegt hoi tegen de gebruiker")
async def hoi(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hoi {interaction.user.mention}! 👋')

@bot.tree.command(name="hallo", description="Groet de gebruiker")
async def hallo(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hallo {interaction.user.mention}, hoe gaat het? 😄')

@bot.tree.command(name="ping", description="Test de bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.tree.command(name="randomgetal", description="Geef een willekeurig getal tussen start en einde")
async def randomgetal(interaction: discord.Interaction, start: int, einde: int):
    import random
    getal = random.randint(start, einde)
    await interaction.response.send_message(f'Het willekeurige getal tussen {start} en {einde} is: {getal}')

# Slash-commando voor contact
@bot.tree.command(name="contact", description="Geef contactinformatie")
async def contact(interaction: discord.Interaction):
    contact_info = """
    Neem contact op met ons via de volgende kanalen:
    📧 E-mail: zierick@jumptechit.nl
    📱 Telefoon: 06-38273136
        Instagram JumpTechIT
        linkedin  Jumptech-it
    """
    await interaction.response.send_message(contact_info)
    
# Start de bot
bot.run("MTM2MTk3NDAzNjQyMjIwMTM4NA.GgA2Pv.afxbiKpRr-EGc6-0Yn9gjFX1t9P1erX9rGdTCU")  # Vergeet je token niet in te vullen!



#oudere versie('s)
""" # Nieuw weercommando
@bot.tree.command(name="weer", description="Haalt de actuele weersomstandigheden op van je weerstation")
async def weer(interaction: discord.Interaction):
    # URL van je weerstation API, vervang deze met de daadwerkelijke URL
    url = "http://145.48.6.82:1337/last/bin"
    
    try:
        # Haal de gegevens op van het weerstation
        response = requests.get(url)
        
        # Controleer of de aanvraag succesvol was
        if response.status_code == 200:
            # Verwerk de ontvangen data (de structuur van je API kan anders zijn)
            data = response.json()
            
            # Verwerk de data (deze zijn slechts voorbeeldnamen, pas aan naar de daadwerkelijke data die je ontvangt)
            temperatuur = data.get('temperature', 'Onbekend')
            luchtvochtigheid = data.get('humidity', 'Onbekend')
            wind_snelheid = data.get('windspeed', 'Onbekend')
            zonnestraling = data.get('solar_radiation', 'Onbekend')
            
            # Verstuur de weerinformatie naar Discord
            await interaction.response.send_message(
                f"🌤 **Actueel Weer** 🌤\n"
                f"Temperatuur: {temperatuur}°C\n"
                f"Luchtvochtigheid: {luchtvochtigheid}%\n"
                f"Wind Snelheid: {wind_snelheid} km/h\n"
                f"Zonnestraling: {zonnestraling} W/m²"
            )
        else:
            await interaction.response.send_message("❌ Fout bij het ophalen van weergegevens.")
    
    except Exception as e:
        await interaction.response.send_message(f"❌ Er is een fout opgetreden: {str(e)}")
    """