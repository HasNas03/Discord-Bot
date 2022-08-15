from forex_python.converter import CurrencyRates
c = CurrencyRates()
import discord, os, random, json, requests, PanclusGz
from PanclusGz import Gz as gz
from reactions import greetings, commands
from datetime import datetime
secret_token = os.environ['TOKEN']

my_ping = "<@" + str(590951005605068810) + ">"

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} has logged in'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  elif message.content.startswith("%hello"):
    await message.channel.send(random.choice(greetings) + str(message.author)[:-5] + "!")
  
  elif message.content.startswith("%motivation"):
    await message.channel.send("You " + str(message.author)[:-5] + ", are a super cool person. I may be a bot but I know a good person when I smell one ;)")
  
  elif message.content.startswith("%jokes"):
    await message.channel.send("Hasan isn't smart enough yet to give me jokes. Wait a few months.")
  
  elif message.content.startswith("%commands"):
    await message.channel.send(commands)
  
  elif message.content.startswith("%days_since"):  
    v_new = message.content[12:20] # actual date portion of the message
    new = datetime.strptime(v_new, '%y/%m/%d') # turn that date into datetime
    diff = datetime.now() - new
    await message.channel.send("It's been " + str(diff.days) + " days since " + str(v_new))
  
  elif message.content.startswith("%curr"):
    currency = message.content[6:9]
    val = c.get_rate('CAD', currency, datetime.now())
    val = round(val, 3)
    await message.channel.send("1 CAD is currently " + str(val) + " " + str(currency))

  elif message.content.startswith("%solar_eclipse"):
    date = gz.date_solar_eclipse()
    await message.channel.send(date)

  elif message.content.startswith("%lunar_eclipse"):
    date = gz.date_lunar_eclipse()
    await message.channel.send(date)
  
  elif my_ping in message.content:
    await message.channel.send("https://tenor.com/view/undertaker-wake-up-gif-14953932")

  elif message.content.startswith("%crypto"):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(key).json
    await message.channel.send(str(f"{data['symbol']} price is {data['price']}"))

client.run(secret_token)
