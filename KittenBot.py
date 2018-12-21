import discord
from RedditApi import get_random_cat
from RedditApi import get_random_kitten

with open("token.txt") as f:
    token = f.read()

class KittenClient(discord.Client):

    async def on_message(self, message):
        if message.content == "k!kittens":
            url = await get_random_kitten()
            emb = discord.Embed().set_image(url=url)
            await self.send_message(message.channel, content="Kittens incoming!", embed=emb)
        elif message.content == "k!cats":
            url = await get_random_cat()
            emb = discord.Embed().set_image(url=url)
            await self.send_message(message.channel, content="Cats incoming!", embed=emb)
        elif message.content == "k!help":
            await self.send_message(message.channel, "I have only two commands: k!kittens and k!cats")

    async def on_ready(self):
        print("Kitten bot ready for action!")


kittenClient = KittenClient()

kittenClient.run(token)
print("Kitten bot down! Send reinforcements!")