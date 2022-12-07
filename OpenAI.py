import openai
import discord

with open('environment.txt') as f:
    lines = f.readlines()

openai.api_key = lines[1]
def createImage(desc):

  response = openai.Image.create(
    prompt = desc,
    n = 1,
    size = "512x512"
  )
  image_url = response['data'][0]['url']
  return image_url

intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  elif message.content.startswith("$generate"):
    work = message.content.split(" ", 1)[1]
    await message.channel.send(createImage(work))

client.run(lines[0])