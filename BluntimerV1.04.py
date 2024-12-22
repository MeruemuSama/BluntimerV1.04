import os
from dotenv import load_dotenv
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
from Bluntimer_Keep_Alive import Bluntimer_Keep_Alive

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
client = discord.Client(intents=intents)


CHANNEL_ID = 1319283636427690035

async def send_alert(message):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(message)

def setup_alerts():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(lambda: asyncio.run(send_alert("L'heure est à 4h20, le THC vous appelle.")),
                      CronTrigger(hour=4, minute=20, second=0))
    
    scheduler.add_job(lambda: asyncio.run(send_alert("L'heure est à 16h20, le THC vous appelle.")),
                      CronTrigger(hour=16, minute=20, second=0))
    
    scheduler.start()

@client.event
async def on_ready():
    print(f"L'entité {client.user} s'est éveillée.")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Le système Bluntimer V1.04 est désormais opérationnel.")
        
    setup_alerts()

Bluntimer_Keep_Alive()
client.run(token)