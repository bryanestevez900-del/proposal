import discord
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_group(group_id):
	value = requests.get("https://games.roblox.com/v2/groups/" + str(group_id) + "/games")
	value = value.json()
	return value["data"]




@client.event
async def on_ready():
    print("Bot is online!")
@client.event
async def on_message(message):
	
	if message.content == "!stats":
		output = ""
		for game in get_group(35106806):
			output += game["name"] + " Has a total of " +  str(game["placeVisits"]) + " visits! " + "\n"

		await message.channel.send(output)
	

client.run("bot token goes in here")