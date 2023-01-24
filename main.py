import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)

GUILD_ID = 500770094100512808
CHANNEL_ID = 1067222475592708197
@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")


  
# name = for your status and url = for your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity=discord.Game(name="Gerichtstermin"))

  



alive.alive()
client.run(os.getenv("TOKEN"), bot=False)

try:
    client.run(os.getenv("TOKEN"), bot=False)
except discord.errors.HTTPException:
    print("Starte Bot neu wegen dem Rate Limit!")
    os.system("kill 1")
    os.system("python restarter.py")
